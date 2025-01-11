"""
    Example project:
        This project represents automatic operation functionality during business hours in
        week

"""

import json
import boto3

client_ec2 = boto3.client('ec2')
client_rds = boto3.client('rds')

resource_start = 'start_business_hours'
resource_stop = 'stop_business_hours'

def lambda_handler(event, context):
    print(event)

    instance_id = 'i-04f6b486835ce37c1'
    rds_id = 'demo-curso'

    turn_on = resource_start in event['resources'][0]
    turn_off = resource_stop in event['resources'][0]

    if turn_on:
        client_ec2.start_instances(InstanceIds=[instance_id])
        client_rds.start_db_instance(DBInstanceIdentifier=rds_id)

        message = 'Instâncias inicializadas'

    if turn_off:
        client_ec2.stop_instances(InstanceIds=[instance_id])
        client_rds.stop_db_instance(DBInstanceIdentifier=rds_id)

        message = 'Instâncias paradas'

    else:
        message = 'Nenhuma instância mudou de estado'

    return {
        'statusCode': 200,
        'body': message
    }
