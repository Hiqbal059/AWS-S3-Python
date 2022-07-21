import boto3
import botocore.exceptions

S3_client = boto3.client(
        's3',
        aws_access_key_id = "",
        aws_secret_access_key = "",
        region_name = ""
    )
    
def get_object(bucket, key):
    """
    This function gets single object from a s3 bucket
    """
    object_data = S3_client.get_object(Bucket=bucket, Key=key)
    result = object_data["Body"].read().decode()
    return result

def upload_file_to_S3(file, bucket_name):
    """
    This function uplaods file to S3 and return access url
    """
    try:
        S3_client.upload_fileobj(file, bucket_name, f"{file}")
        file_url = f"https://{bucket_name}.s3.us-west-2.amazonaws.com/{file}"
        return file_url
    except botocore.exceptions as e:
        print(e)
