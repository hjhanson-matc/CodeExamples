import boto3,argparse

client = boto3.client('ec2')

parser = argparse.ArgumentParser(description="Arguments for getting security group information")
parser.add_argument('-s','--security-group',dest='sg_name',default='',type=str,help='Enter the name of a security group.')

args=parser.parse_args()

if not args.sg_name:
    response = client.describe_security_groups()
    print("Here are your security groups:\n")
    for sg in response['SecurityGroups']:
        print(sg['GroupName'])
        for ip in sg['IpPermissions']:
            print(ip['IpRanges'])
            for key in ip['IpRanges']:
                if key['CidrIp'] == '0.0.0.0/0' or key['CidrIp'] == '0.0.0.0':
                    print(f"{sg['GroupName']} is open to the public internet!")
                else:
                    pass
        print()

else:
    response = client.describe_security_groups(
        Filters=[
            {
                'Name': 'group-name',
                'Values':[args.sg_name]
            }
        ]
    )
    print(f"Here is the info for {args.sg_name}:\n")
    for sg in response['SecurityGroups']:
        print(sg['GroupName'])
        for ip in sg['IpPermissions']:
            print(ip['IpRanges'])
            for key in ip['IpRanges']:
                if key['CidrIp'] == '0.0.0.0/0' or key['CidrIp'] == '0.0.0.0':
                    print(f"{sg['GroupName']} is open to the public internet!")
                else:
                    pass
        print()