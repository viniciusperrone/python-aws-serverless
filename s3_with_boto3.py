import boto3
import os

from dotenv import load_dotenv

load_dotenv()

session = boto3.Session(profile_name=os.getenv('AWS_PROFILE_NAME'))
client_s3 = session.client('s3')

bucket_name = 'aws-python-course'
bucket_region = 'us-east-2'

try:
    response_bucket = client_s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': bucket_region
        }
    )

    print(response_bucket)
except Exception as e:
    print('This bucket already exist!')

response_upload = client_s3.upload_file(
    'static_files/aws_logo_smile.png',
    bucket_name,
    'images/aws_logo_smile.png'
)

