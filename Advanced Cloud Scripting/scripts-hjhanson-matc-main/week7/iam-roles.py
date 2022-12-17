import boto3,datetime,pytz

client = boto3.client('iam')

response = client.list_roles()

Rolenames = []

print("The following roles where created in the past 90 days:\n")
for roles in response['Roles']:
    if roles['CreateDate'] > (pytz.utc.localize(datetime.datetime.utcnow())-datetime.timedelta(days=90)):
        Rolenames.append(roles['RoleName'])
        print("Role Name:",roles['RoleName'])
        print("Creation Date:",roles['CreateDate'])
        for obj in Rolenames:
            policyresponse = client.list_role_policies(RoleName=obj)
            print("Policy Names:",policyresponse['PolicyNames'])
            Rolenames = []
            
        print()

