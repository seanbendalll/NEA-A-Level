#downloading an image
import boto3
from botocore import UNSIGNED
from botocore.config import Config

def find_bucket_key(s3_path):
    """
    This is a helper function that given an s3 path such that the path is of
    the form: bucket/key
    It will return the bucket and the key represented by the s3 path
    """
    s3_components = s3_path.split('/')
    bucket = s3_components[0]
    s3_key = ""
    if len(s3_components) > 1:
        s3_key = '/'.join(s3_components[1:])
    return bucket, s3_key


def split_s3_bucket_key(s3_path):
    """Split s3 path into bucket and key prefix.
    This will also handle the s3:// prefix.
    :return: Tuple of ('bucketname', 'keyname')
    """
    if s3_path.startswith('s3://'):
        s3_path = s3_path[5:]
    return find_bucket_key(s3_path)
bucket_name, key_name = split_s3_bucket_key(
    'us-west-2.amazonaws.com/secure.notion-static.com/dfa21f8d-60a8-437b-86c4-bc552eedf56b/Screenshot_2021-04-01_at_10.29.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220129T114137Z&X-Amz-Expires=3600&X-Amz-Signature=eecab75ef22b64384b4663800aa0c6d887284fd72e4a615fbba76403892359c4&X-Amz-SignedHeaders=host&x-id=GetObjectdo')
client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
response = client.get_object(Bucket=bucket_name, Key=key_name)
