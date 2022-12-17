import boto3, botocore
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
        #SecurityGroups=['WebSG'],
        UserData='''
            #!/bin/bash -ex
            # Updated to use Amazon Linux 2
            yum -y update
            yum -y install httpd php mysql php-mysql
            /usr/bin/systemctl enable httpd
            /usr/bin/systemctl start httpd
            cd /var/www/html
            wget https://aws-tc-largeobjects.s3-us-west-2.amazonaws.com/CUR-TF-100-ACCLFO-2/lab6-scaling/lab-app.zip
            unzip lab-app.zip -d /var/www/html/
            chown apache:root /var/www/html/rds.conf.php
            ''',
        MaxCount=1,
        MinCount=1,
        DryRun=DRYRUN
    )
    return response['Instances'][0]['InstanceId']

def main():
    try:
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
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'UnauthorizedOperation':
            print("You do not have authorization to create ec2 instances in this region.\nPlease check your AWS config.")
        # If you credentials are incorrect or you otherwise don't have permission to preform an action it will throw an
        # AuthFailure error, to handle the exeption I am just piggy backing off the except I already have and adding another
        # if statement.
        elif error.response['Error']['Code'] == 'AuthFailure':
            print("You are not authorized to preform the action, please check that your credentials are correct and you have permission to preform the action.")
        else:
            print(f"The following error has occured: {error}")


if __name__ == "__main__":
    main()