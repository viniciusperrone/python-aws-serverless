import boto3
import os

from dotenv import load_dotenv

load_dotenv()

# Credentials
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_KEY_ACCESS')

profile_name = os.getenv('AWS_PROFILE_NAME')
region_name = os.getenv('AWS_REGION')

session = boto3.Session(profile_name=profile_name, region_name='us-east-1')
client_ec2 = session.client('ec2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

instance_ids = ['i-0c4c859a4c3c3df49', 'i-0571536c49aaa9f9b']

try:
    response = client_ec2.terminate_instances(
        InstanceIds=instance_ids
    )

    print(response)

except Exception as e:
    print(e)
