import boto3, json, datetime

client = boto3.client('s3')
bucket_name = "hjhanson-script2-week2-f22"

bucket_response = client.create_bucket(Bucket=bucket_name)

bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': "arn:aws:s3:::%s/*" % bucket_name
    }]
}
bucket_policy_string = json.dumps(bucket_policy)

response = client.put_bucket_policy(
    Bucket=bucket_name,
    Policy=bucket_policy_string
)
put_bucket_response = client.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
    }
)

indexFile = open('index.html', 'rb')
put_index_response = client.put_object(Body=indexFile,Bucket=bucket_name,Key='index.html',ContentType='text/html')
indexFile.close()
print (put_index_response)

errorFile = open('error.html', 'rb')
put_error_response = client.put_object(Body=errorFile,Bucket=bucket_name,Key='error.html',ContentType='text/html')
errorFile.close()
print (put_error_response)