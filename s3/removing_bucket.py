from main import bucket_name, session

resource_s3 = session.resource("s3")
bucket = resource_s3.Bucket(bucket_name)

bucket.delete()
