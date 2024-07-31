import boto3
import os

from dotenv import load_dotenv

load_dotenv()

session = boto3.Session(profile_name=os.getenv('AWS_PROFILE_NAME'))
client_s3 = session.client('s3')

try:
    response_bucket = client_s3.create_bucket(
        Bucket='aws-python-course',
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )

    print(response_bucket)
except Exception as e:
    print('This bucket already exist!')


