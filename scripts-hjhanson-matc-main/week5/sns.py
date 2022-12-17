import boto3

def CreateSNSTopic(TopicName):
    sns_client = boto3.client('sns')
    response = sns_client.create_topic(Name=TopicName)
    return response['TopicArn']

def SubscribeEmail(topic_arn,email):
    sns_client = boto3.client('sns')
    response = sns_client.subscribe(TopicArn=topic_arn,Endpoint=email,Protocol='email')
    return response['SubscriptionArn']

