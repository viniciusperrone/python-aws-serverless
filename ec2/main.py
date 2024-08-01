import boto3
import os

from dotenv import load_dotenv

load_dotenv()

profile_name = os.getenv('AWS_PROFILE_NAME')
region_name = os.getenv('AWS_REGION')
key_pair = os.getenv('AWS_KEY_PAIR')
vpc_id = os.getenv('AWS_VPC_ID')
subnet_id = os.getenv('AWS_SUBNET_ID')
ami_id = os.getenv('AWS_AMI_ID')

session = boto3.Session(profile_name=profile_name, region_name=region_name)

client_ec2 = session.client('ec2')

try:
    response_sg = client_ec2.create_security_group(
        Description='New sg',
        GroupName='sg_web',
        VpcId=vpc_id
    )

    sg_id = response_sg['GroupId']
except Exception as err:
    print('This security group already exists!')
    response_group_sg = client_ec2.describe_security_groups(
        GroupNames=['sg_web']
    )

    sg_id = response_group_sg['SecurityGroups'][0]['GroupId']


try:
    response_ingress = client_ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'ToPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Access SSH'
                    }
                ]
            },
            {
                'FromPort': 80,
                'ToPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Access HTTP'
                    }
                ]
            }
        ]
    )

    print(response_ingress)
except Exception as err:
    print(err)
