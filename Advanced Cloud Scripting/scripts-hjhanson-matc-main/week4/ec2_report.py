import boto3,csv

def Get_Instances(name,values):
    ec2_client = boto3.client('ec2')
    paginator = ec2_client.get_paginator('describe_instances')
    page_list = paginator.paginate(
        Filters=[
            {
                'Name': name,
                'Values': [
                    values,
                ]
            },
        ],
    )
    response = []
    for page in page_list:
        for reservation in page['Reservations']:
            response.append(reservation)
    return response

def CSV_Writer(header, content):
    hFile = open('export.csv', 'w')
    writer = csv.DictWriter(hFile,fieldnames=header)
    writer.writeheader()
    for line in content:
        writer.writerow(line)
    hFile.close()

def main():
    
    FilterName = 'instance-type'
    FilterValues = 't2.micro'
    response = Get_Instances(FilterName, FilterValues)
    headerRow = ('InstanceId', 'InstanceType', 'State', 'PublicIpAddress', 'Monitoring')
    content = []
    for instance in response:
        for ec2 in instance['Instances']:
            content.append(
                {
                    "InstanceId": ec2['InstanceId'],
                    "InstanceType": ec2['InstanceType'],
                    "State": ec2['State']['Name'],
                    "PublicIpAddress": ec2.get('PublicIpAddress', "N/A"),
                    "Monitoring": ec2['Monitoring']['State']
                }

            )
    CSV_Writer(headerRow,content)



if __name__ == "__main__":
    main()

