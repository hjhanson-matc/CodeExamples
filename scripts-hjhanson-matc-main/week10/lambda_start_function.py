import json, boto3

def Start_EC2():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:env',
                'Values': ['dev']
            }
        ]
    )
    instance_list = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])
    start_response = ec2.start_instances(InstanceIds=instance_list)
    return start_response

def lambda_handler(event, context):
    # TODO implement
    response = Start_EC2()
    for instance in response['StartingInstances']:
        print(instance['InstanceId'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
