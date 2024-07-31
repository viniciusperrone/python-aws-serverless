import boto3
import os

from dotenv import load_dotenv

load_dotenv()

# Create a session
session = boto3.Session(profile_name=os.getenv('AWS_PROFILE_NAME'))

client_s3 = session.client('s3')
client_ec2 = session.client('ec2')

list_buckets = client_s3.list_buckets()

resource_s3 = session.resource('s3')
bucket = resource_s3.Bucket('any_bucket')

print(resource_s3)
