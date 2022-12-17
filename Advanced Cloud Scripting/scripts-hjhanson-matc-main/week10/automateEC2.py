import boto3

ec2 = boto3.client('ec2')

def Stop_EC2():
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
    stop_response = ec2.stop_instances(InstanceIds=instance_list)
    return stop_response

def Start_EC2():
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

def main():
    print(Start_EC2())

if __name__ == "__main__":
    main()