# This script will retrieve and list user managed and attached IAM policies name, attachment count, update/creation date, and tags.
import boto3,argparse

client = boto3.client('iam')

# This call will filter user scope and unattached policies.
response = client.list_policies(Scope='Local',OnlyAttached=True)

print("The following user managed policies exist on your account:\n")

# Now to iterate through the dictionary response and pick out what I want.
for policy in response['Policies']:
    print("Policy name:",policy['PolicyName'])
    print("Number of attachments:",policy['AttachmentCount'])
    # Only need to check UpdateDate since if a policy hasn't been updated, it will display the creation date.
    print("The policy was last changed:",policy['UpdateDate'])
    print("Tags associated with this policy: ",end="")
    # Need to use a try except for the tags since if a policy has no tags the response won't have a tags section causing a key error.
    try:
        for tags in policy['Tags']:
            print(f"{tags['Key']} : ",end="")
            print(tags['Value'])
    except:
        print("This policy has no tags!")
    print()