## import boto3
import boto3
from pprint import pprint
## Open Management console
aws_management_console = boto3.session.Session(profile_name="default")

## Open IAM Console
iam_console = aws_management_console.client(service_name='iam')

##List users
output=iam_console.list_users()

#pprint(output['Users'])

for users in output['Users']:
    print(users['UserName'])
