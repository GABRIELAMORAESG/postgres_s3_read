import boto3
from botocore.exceptions import ClientError
import pandas as pd
import csv
import configparser


def read_s3_csv(bucket_name, file_name, region_name):
    try:
        # Create an S3 client
        s3_client = boto3.client('s3', region_name=region_name)
        
        # Read the CSV file from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        
        # Read the CSV data into a DataFrame
        csv_data = pd.read_csv(response['Body'])
        
        return csv_data
    
    except ClientError as e:\
            print(f"An error occurred: {e}")

def main():
    try:
        # Read configurations from dwh.cfg
        config = configparser.ConfigParser()
        config.read('s3/dwh.cfg')
        aws_config = config['AWS']
        bucket_name = aws_config['bucket_name']
        file_name = aws_config['file_name']
        region_name = aws_config['region_name']

        # Read the CSV file from S3 into a DataFrame
        df = read_s3_csv(bucket_name, file_name, region_name)

        if df is not None:
            # Write the DataFrame to a new CSV file
            with open('s3/account_creation_event.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(df.columns)  # Write header
                rows_written = 0
                for index, row in df.iterrows():
                    writer.writerow(row)
                    rows_written += 1

                print(f"Number of rows written: {rows_written}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()