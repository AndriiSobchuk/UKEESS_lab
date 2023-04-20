TASK: AWS Lambda - Handle S3 bucket creation: Write a Lambda function that triggers when an S3 bucket object is created and performs a specific action.

Description:

Here we have only lambda.py file where we initializing S3 client and handle events inside it with function "lambda_handler". In general if object exists inside S3 bucket we will get the output: "datatime + ' _UKEESS_ ' + bucket + ' ' + key'". In bad scenario we will get exception error.

**Highly important to mention**: to make S3 bucket accessible for Lambda function we should create/edit role which has permissions for: `s3:GetObject`, `s3:ListBucket`.
