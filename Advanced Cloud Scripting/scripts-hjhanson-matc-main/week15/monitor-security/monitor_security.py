import boto3,time

client = boto3.client('ec2')

response = client.describe_instances()
GroupIds = []
for Dict in response['Reservations']:
    for Instances in Dict['Instances']:
        for SecurityGroups in Instances['SecurityGroups']:
            GroupIds.append(SecurityGroups['GroupId'])

for item in GroupIds:
    print(f"Checking the security group {item} for open port 22")
    time.sleep(2)
    response = client.describe_security_groups(
        GroupIds=[
            item
        ]
    )
    for SGs in response['SecurityGroups']:
        if SGs['IpPermissions']:
            for IpInfo in SGs['IpPermissions']:
                if IpInfo['FromPort'] == 22:
                    for IP in IpInfo['IpRanges']:
                        if IP['CidrIp'] == '0.0.0.0/0':
                            print(f"{item}'s port 22 is open to the internet!")
                            print("Revoking port 22 access")
                            response = client.revoke_security_group_ingress(
                                CidrIp='0.0.0.0/0',
                                FromPort=22,
                                GroupId=item,
                                IpProtocol='tcp',
                                ToPort=22,
                            )
                            print()
                        else:
                            print(f"{item} has a port 22 rule set up, but it is not open to the internet")
                            print()
                else:
                    print(f"{item} does not have any port 22 rules set up")
                    print()
        else:
            print(f"{item} does not have any ingress rules")
            print()
