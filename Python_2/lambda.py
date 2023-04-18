import boto3
import datetime

# Initialize S3 client
s3Client = boto3.client('s3')


# Handler event function
def lambda_handler(event, context):
    print(event)
    # Get the bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(bucket)
    print(key)
    now = datetime.datetime.now()

    try:
        # Get object from S3 bucket
        response = s3Client.get_object(Bucket=bucket, Key=key)
        print(str(now) + ' _UKEESS_ ' + bucket + ' ' + key)
    except Exception as e:
        print(f"Error: {e}")
