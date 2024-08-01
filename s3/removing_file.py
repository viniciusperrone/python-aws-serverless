from main import bucket_name, client_s3, session

key_image = "images/Python.jpeg"

# Deleting single file
client_s3.delete_object(
    Bucket=bucket_name,
    Key=key_image
)

# Deleting multiple files
resource_s3 = session.resource("s3")
bucket = resource_s3.Bucket(bucket_name)

bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': 'names.xls'
            },
            {
                'Key': 'Senha AWS.txt'
            }
        ]
    }
)

# Deleting all files in Bucket
objects = bucket.objects.all()

objects.delete()
