import boto3
import json
import datetime

def defaultconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

client = boto3.client('s3')

bucket_response = client.list_buckets()

#print(json.dumps(response,default=defaultconverter,indent=4))

for bucket in bucket_response['Buckets']:
    print(f"Bucket {bucket['Name']} found!")
    object_response = client.list_objects(Bucket=bucket['Name'])
    try:
        for object in object_response['Contents']:
            print(f"The object {object['Key']} exists in {bucket['Name']}.")
    except:
        print("This bucket contains no objects.")
    print ("-" *30)