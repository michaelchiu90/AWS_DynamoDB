import boto3
from pprint import pprint
s3 = boto3.client('s3')

def list_buckets():
    # Output the bucket names
    response = s3.list_buckets()
    print('Existing buckets:')

    for bucket in response['Buckets']:
        print(f' {bucket["Name"]}')

list_buckets()

#output: Existing buckets:
#       polyuawslab-michaelchiu