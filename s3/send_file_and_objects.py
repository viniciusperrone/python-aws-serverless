from main import client_s3, bucket_name

client_s3.upload_file(
    'static_files/aws_logo_smile.png',
    bucket_name,
    'images/aws_logo_smile.png'
)

spreadsheet = """
    Name\tNome
    Ana\t8
    Mario\t9
    Maria\t7
    Carlos\t10
"""

client_s3.put_object(
    Body=spreadsheet,
    Bucket=bucket_name,
    Key='names.xls'
)
