import csv

#########################################################################################################
############################ This script will perfom csv reader and writer ##############################
#####################################    Author : Arun Reddy       ######################################
#########################################################################################################

def filter_sales(input_file, output_file, target_year):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            date = row[3]  
            if date.startswith(target_year):
                writer.writerow(row)

def main():
    input_file = input("Enter the input CSV file path: ")
    output_file = input("Enter the output CSV file path: ")
    target_year = input("Enter the target year: ")

    filter_sales(input_file, output_file, target_year)

main()
