import boto3

session = boto3.Session(profile_name="automation-course")
client_s3 = session.client('s3')

list_client = client_s3.list_buckets()

print(list_client)
