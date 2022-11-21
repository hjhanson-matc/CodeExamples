import json,boto3

def Stop_EC2():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instance_list = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])
    stop_response = ec2.stop_instances(InstanceIds=instance_list)
    return stop_response

def lambda_handler(event, context):
    # TODO implement
    response = Stop_EC2()
    for instance in response['StoppingInstances']:
        print(instance['InstanceId'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
