# AWS-S3-Python
Python code to get and create items on AWS-S3 buckets 

# Install Package
```
pip install boto3
```

# Create S3 Client 
```
S3_client = boto3.client(
        's3',
        aws_access_key_id = "",
        aws_secret_access_key = "",
        region_name = ""
    )
```

# Create object on S3 using client
```
def upload_file_to_S3(file, bucket_name, region_name):
    """
    This function uplaods file to S3 and return access url
    """
    try:
        S3_client.upload_fileobj(file, bucket_name, f"{file}")
        file_url = f"https://{bucket_name}.s3.{region_name}.amazonaws.com/{file}"
        return file_url
    except botocore.exceptions as e:
        print(e)
```

# Get Object from S3 bucket
```
def get_object(bucket, key):
    """
    This function gets single object from a s3 bucket
    """
    object_data = S3_client.get_object(Bucket=bucket, Key=key)
    result = object_data["Body"].read().decode()
    return result
```
