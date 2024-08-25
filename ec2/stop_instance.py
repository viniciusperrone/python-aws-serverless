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

try:
    response_instances = client_ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running'
                ]
            },
        ]
    )


    instance_ids = [
        instance['InstanceId']
        for reservation in response_instances['Reservations']
        for instance in reservation['Instances']
    ]

    print(instance_ids)

except Exception as e:
    instance_ids = None

    print(e)

if instance_ids is not None:
    response = client_ec2.stop_instances(InstanceIds=instance_ids)
