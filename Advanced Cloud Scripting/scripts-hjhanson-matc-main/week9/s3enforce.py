import boto3

def CreateBucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
    return response

def DeleteBucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.delete_bucket(Bucket=bucket_name)
    return response

def EnforceS3Encryption(bucket_name):
    s3 = boto3.client('s3')
    response = s3.put_bucket_encryption(
        Bucket = bucket_name,
        ServerSideEncryptionConfiguration= {
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm' : 'AES256'
                    }
                }
            ]
        }
    )
    return response

def SetBucketPolicy(bucket_name, policy):
    s3 = boto3.client('s3')
    response = s3.put_bucket_policy(Bucket=bucket_name, Policy=policy)
    return response

def main():
    bucket_name = "hhanson22-test-bucket-s3"
    create_response = CreateBucket(bucket_name)
    print(f"Created: {create_response}")

    encrypt_response = EnforceS3Encryption(bucket_name)
    print(f"Encrypted: {encrypt_response}")

if __name__ == "__main__":
    main()