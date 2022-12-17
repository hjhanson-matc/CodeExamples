import boto3, s3enforce, json

sts_client = boto3.client("sts")
account_id = sts_client.get_caller_identity()["Account"]

def CreateTrail(trail_name, bucket_name):
    trail = boto3.client('cloudtrail')
    try:
        create_response = trail.create_trail(Name=trail_name, S3BucketName=bucket_name)
        log_response = trail.start_logging(Name=trail_name)
        return log_response
    except trail.exceptions.TrailAlreadyExistsException as error:
        return "Trail Already Exists"
    except:
        return "Some other error has occured"

def main():
    bucket_name = "hhanson1-trail-bucket"
    trail_name = "hhanson-cloud-trail"

    create_response = s3enforce.CreateBucket(bucket_name)

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AWSCloudTrailAclCheck20150319",
                "Effect": "Allow",
                "Principal": {"Service": "cloudtrail.amazonaws.com"},
                "Action": "s3:GetBucketAcl",
                "Resource": f"arn:aws:s3:::{bucket_name}"
            },
            {
                "Sid": "AWSCloudTrailWrite20150319",
                "Effect": "Allow",
                "Principal": {"Service": "cloudtrail.amazonaws.com"},
                "Action": "s3:PutObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/AWSLogs/{account_id}/*",
                "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
            }
        ]
    }

    bucket_policy_response = s3enforce.SetBucketPolicy(bucket_name,json.dumps(policy))
    response = CreateTrail(trail_name,bucket_name)

if __name__ == "__main__":
    main()