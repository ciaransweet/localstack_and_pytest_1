import json
import os
from zipfile import ZipFile

import boto3
import botocore

CONFIG = botocore.config.Config(retries={'max_attempts': 0})
LAMBDA_ZIP = './lambda.zip'


def get_lambda_client():
    return boto3.client(
        'lambda',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='eu-west-2',
        endpoint_url='http://localstack:4574',
        config=CONFIG
    )


def create_lambda_zip(function_name):
    with ZipFile(LAMBDA_ZIP, 'w') as z:
        z.write(function_name + '.py')


def create_lambda(function_name):
    lambda_client = get_lambda_client()
    create_lambda_zip(function_name)
    with open(LAMBDA_ZIP, 'rb') as f:
        zipped_code = f.read()
    lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.6',
        Role='role',
        Handler=function_name + '.handler',
        Code=dict(ZipFile=zipped_code)
    )


def delete_lambda(function_name):
    lambda_client = get_lambda_client()
    lambda_client.delete_function(
        FunctionName=function_name
    )
    os.remove(LAMBDA_ZIP)


def invoke_function_and_get_message(function_name):
    lambda_client = get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse'
    )
    return json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )
