import boto3
import os

from dotenv import load_dotenv

load_dotenv()

session = boto3.Session(profile_name=os.getenv('AWS_PROFILE_NAME'))
client_s3 = session.client('s3')

bucket_name = 'aws-python-course'
bucket_region = 'us-east-2'
