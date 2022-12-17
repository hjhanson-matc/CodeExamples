import boto3
DRYRUN = False

def Get_Image(ec2_client):
    image_response = ec2_client.describe_images(
        Filters=[
            {
                'Name':'description',
                'Values':['Amazon Linux 2 AMI*']
            },
            {
                'Name':'architecture',
                'Values':['x86_64']
            },
            {
                'Name':'owner-alias',
                'Values':['amazon']
            }
        ]
    )
    return image_response['Images'][0]['ImageId']

def Create_EC2(ec2_client, AMI):
    response = ec2_client.run_instances(
        ImageId=AMI,
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        DryRun=DRYRUN
    )
    return response['Instances'][0]['InstanceId']

def main():
    client = boto3.client('ec2')
    AMI = Get_Image(client)
    instance_id = Create_EC2(client, AMI)
    ec2_instance = boto3.resource('ec2')
    ec2 = ec2_instance.Instance(instance_id)
    print(f"instance is {ec2.state['Name']}")
    print("Waiting for instance to run....")
    ec2.wait_until_running()
    print("Instance is now up and running....")
    ec2.load()
    print(f"The instance id is: {instance_id}")
    print(f"The public IP of the instance is: {ec2.public_ip_address}")
    print(f"The instance has the following tags\n{ec2.tags}")
    ec2.create_tags(
        Resources=[
            (instance_id),
        ],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'Hunter'
            },
        ]
    )
    ec2.load()
    print(f"The instance now has the following tags\n{ec2.tags}")
    cleanup = input("Would you like to terminate the instance?(y/n):")
    if cleanup == "y":
        print("The instance will now terminate!")
        ec2.terminate()
        print("Waiting for instance to terminate...")
        ec2.wait_until_terminated()
        print(f"instance is {ec2.state['Name']}")
    elif cleanup == "n":
        exit()
    else:
        print ("Invalid response, instance will not terminate.")

if __name__ == "__main__":
    main()