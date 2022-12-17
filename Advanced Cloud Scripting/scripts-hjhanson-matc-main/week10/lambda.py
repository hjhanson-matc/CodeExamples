import boto3, time

lambda_client = boto3.client('lambda')
iam = boto3.client('iam')

def Create_Lambda(function_name):
    role_response = iam.get_role(RoleName='LabRole')
    handler = open('lambda_start_function.zip', 'rb')
    zipped_code = handler.read()
    response = lambda_client.create_function(
        FunctionName = function_name,
        Role = role_response['Role']['Arn'],
        Publish = True,
        PackageType = 'Zip',
        Runtime = 'python3.9',
        Code = {
            'ZipFile': zipped_code
        },
        Handler = 'lambda_start_function.lambda_handler'
    )

def Invoke_Lambda(function_name):
    invoke_response = lambda_client.invoke(FunctionName=function_name)
    return invoke_response

def main():
    functionname = 'startEC2'
    try:
        function = lambda_client.get_function(FunctionName=functionname)
        print("Function Already Exists")
    except:
        print("Creating Function")
        response = Create_Lambda(functionname)
        time.sleep(5)
    print("Invokeing Lambda Function")
    Invoke_Lambda(functionname)


if __name__ == "__main__":
    main()