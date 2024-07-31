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

client_s3.upload_file(
    'static_files/aws_logo_smile.png',
    bucket_name,
    'images/aws_logo_smile.png'
)

spreadsheet = """
    Name\tNome
    Ana\t8
    Mario\t9
    Maria\t7
    Carlos\t10
"""

client_s3.put_object(
    Body=spreadsheet,
    Bucket=bucket_name,
    Key='names.xls'
)
