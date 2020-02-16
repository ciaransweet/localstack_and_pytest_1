import boto3
import logging
import os
from datetime import datetime

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
IS_PROD = os.environ['STAGE'] == 'PRODUCTION'


def get_s3_client():
    if IS_PROD:
        return boto3.client('s3')
    else:
        return boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', region_name='eu-west-2',
                            endpoint_url='http://172.17.0.1:4572')


S3_CLIENT = get_s3_client()


def handler(event, context):
    LOGGER.info('I\'m putting something in S3')
    test_object_key = 'a-object-{0}'.format(datetime.now().isoformat())
    S3_CLIENT.put_object(
        Bucket='a-bucket',
        Key=test_object_key,
        Body='some body'
    )
    return {
        "message": "{0} placed into S3".format(test_object_key)
    }
