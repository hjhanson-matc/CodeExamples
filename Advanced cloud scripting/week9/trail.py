import boto3, s3enforce, json, time

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

def StartLogging(trail_name):
    trail = boto3.client('cloudtrail')
    response = trail.start_logging(Name=trail_name)
    return response

def StopLogging(trail_name):
    trail = boto3.client('cloudtrail')
    response = trail.stop_logging(Name=trail_name)
    return response

def GetTrailStatus(trail_name):
    trail = boto3.client('cloudtrail')
    try:
        response = trail.get_trail_status(Name=trail_name)
        return response['IsLogging']
    except trail.exceptions.TrailNotFoundException as error:
        print("That trail name does not exist")
        raise NameError("That CloudTrail Trail was not found")
    except:
        print("Some other error has occured")

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
    stop_response = StopLogging(trail_name)
    time.sleep(5)
    if GetTrailStatus(trail_name):
        print("Trail is logging as expected")
    else:
        print("Trail is NOT logging, something is wrong")

if __name__ == "__main__":
    main()