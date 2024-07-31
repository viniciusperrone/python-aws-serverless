from main import client_s3, bucket_name

image_url = "images/Python.jpeg"

client_s3.download_file(
    bucket_name,
    image_url,
    "static_files/python.jpeg"
)
