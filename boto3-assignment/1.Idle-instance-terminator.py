import boto3
import datetime

#########################################################################################################
################ This script will list all EC2 instances with low CPU and N/w consumpion and ############
########################### terminate the instances after taking snapshot ###############################
#####################################    Author : Arun Reddy       ######################################
#########################################################################################################

ec2_client = boto3.client('ec2')
cloudwatch_client = boto3.client('cloudwach')
####low_util_instances = []


def identify_low_utilization(Pass-the-arguments-here) :
#calculate utilization here
    now = datetime.datetime.utcnow()
    start_time = now - datetime.timedelta(days=days)
    low_util_instances = []

    response = ec2_client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id=instance['InstanceId']

            ## Check CPU Utilization
            cpu_stats = cloudwatch_client.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=start_time,
                    EndTime=now,
                    Period=period,
                    Statistics=['Average']
            )
            # Check Network Utilization
            network_in_stats = cloudwatch_client.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='NetworkIn',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=start_time,
                    EndTime=now,
                    Period=period,
                    Statistics=['Average']
            )
            
            network_out_stats = cloudwatch_client.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='NetworkOut',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=start_time,
                    EndTime=now,
                    Period=period,
                    Statistics=['Average']
            )
            if cpu_stats['Datapoints']:
                cpu_util = cpu_stats['Datapoints'][0]['Average']
            else:
                cpu_util = 0
            network_in_util = network_in_stats['Datapoints'][0]['Average'] if network_in_stats['Datapoints'] else 0
            network_out_util = network_out_stats['Datapoints'][0]['Average'] if network_out_stats['Datapoints'] else 0

            ### check if the utiliztion is less than defined threshold 
            if cpu_util < threshold_cpu and (network_in_util + network_out_util) < threshold_network:
                low_util_instances.append(instance_id)
    return low_util_instances
    print("The list of all Available instances are ")

def snapshot_and_termination(instance_ids,create_snapshot=True):

    # volumeids = []
    # response = ec2_client.describe_instances()
    # for reservation in response['Reservations']:
	# for instance in reservation['Instances']:
	# 	for block in instance['BlockDeviceMappings']:
	# 		volumeid = block['Ebs']['VolumeId']
	# 		volumeids.append(volumeid)

    for instance_id in instance_ids:
        print(f"Now Processing Instance : {instance}")

        if create_snapshot:
            volumes = ec2_client.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])
            for volume in volumes['Volumes']:
                volume_id = volume['VolumeId']
                print(f"Creating snapshot for volume: {volume_id}")
                ec2_client.create_snapshot(VolumeId=volume_id, Description=f"Snapshot of {instance_id} before termination")
        
        print(f"Terminating instance: {instance_id}")
        ec2_client.terminate_instances(InstanceIds=[instance_id])
         
#take snapshots and terminate the instances here


def main() :
    low_util_instances = identify_low_utilization()
    if low_util_instances:
        print(f"Instances with low utilization are : {low_util_instances}")
        snapshot_and_terminate(low_util_instances)
    else:
        print("There are no Idle instances")
    
main()
