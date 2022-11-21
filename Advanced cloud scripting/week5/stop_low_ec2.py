import boto3, ec2, sns

DRYRUN = False

sts_client = boto3.client("sts")
account_id = sts_client.get_caller_identity()["Account"]

ec2_client = boto3.client('ec2')
image_id = ec2.Get_Image(ec2_client)

instance_id = ec2.Create_EC2(ec2_client, image_id)
print (f"Instance ID: {instance_id}")

cw_client = boto3.client('cloudwatch')

sns_topic = sns.CreateSNSTopic("low-notification")
response = sns.SubscribeEmail(sns_topic, 'hjhanson@madisoncollege.edu')

response = cw_client.put_metric_alarm(
    AlarmName='Web_Server_LOW_CPU_Utilization',
    ComparisonOperator='LessThanOrEqualToThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=300,
    Statistic='Average',
    Threshold=10.0,
    ActionsEnabled=True,
    AlarmActions=[
        f'arn:aws:swf:us-east-1:{account_id}:action/actions/AWS_EC2.InstanceId.Stop/1.0',
        f'arn:aws:sns:us-east-1:{account_id}:low-notification'
    ],
    AlarmDescription='Alarm when server CPU is lower than 10%',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ]

)