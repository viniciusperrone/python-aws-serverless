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

def get_sg_id() -> str:
    try:
        response_sg = client_ec2.create_security_group(
            Description='New sg',
            GroupName='sg_web',
            VpcId=vpc_id
        )

        sg_id = response_sg['GroupId']

    except Exception as err:
        print("This security group already exist!")

        response_group_sg = client_ec2.describe_security_groups(
            GroupNames=['sg_web']
        )

        sg_id = response_group_sg['SecurityGroups'][0]['GroupId']

    return sg_id

def add_ingress_rules(sg_id: str):
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

    except Exception as err:
        print(err)


    return

sg_id = get_sg_id()

# add_ingress_rules(sg_id)
# Get path of target file

filename_target = 'wp_user_data.sh'
path_file_target = os.path.join(os.path.dirname(__file__), 'commands', filename_target)

file_user_data = open(path_file_target, 'r')

user_data = file_user_data.read()

file_user_data.close()

try:
    response_ec2 = client_ec2.run_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'VolumeSize': 8,
                    'DeleteOnTermination': True,
                    'VolumeType': 'gp2',
                    'Encrypted': False
                }
            }
        ],
        UserData=user_data,
        ImageId=ami_id,
        MaxCount=1,
        MinCount=1,
        InstanceType='t2.micro',
        KeyName=key_pair,
        Monitoring={
            'Enabled': False
        },
        SecurityGroupIds=[sg_id],
        SubnetId=subnet_id,
        InstanceInitiatedShutdownBehavior='terminate',
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'wp-course-python'
                    },
                    {
                        'Key': 'Environment',
                        'Value': 'development'
                    }
                ]
            }
        ]
    )

    print("response_ec2: ", response_ec2)
except Exception as err:
    print(err)
