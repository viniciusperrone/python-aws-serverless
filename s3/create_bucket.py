from main import client_s3, bucket_name, bucket_region

try:
    response_bucket = client_s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': bucket_region
        }
    )

    print(response_bucket)
except Exception as e:
    print('This bucket already exist!')
