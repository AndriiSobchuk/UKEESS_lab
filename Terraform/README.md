TASK: "AWS Lambda: Create a Terraform configuration that provisions an AWS Lambda function and an API Gateway endpoint that triggers the Lambda function. The configuration should include appropriate IAM roles and permissions."

Description:

Here I've been following official Terraform guide: https://developer.hashicorp.com/terraform/tutorials/aws/lambda-api-gateway to solve current task.
So all we need is to setup IAM user with the following permissions policies (`AmazonAPIGatewayAdministrator`, `AmazonS3FullAccess`, `AWSLambda_FullAccess`, `CloudWatchLogsFullAccess`, `IAMFullAccess`) and made `aws configure` to provide access key, secret access key and region.

As a result after launching `terraform apply` and checking the result with the command: `curl "$(terraform output -raw base_url)/hello?Name=Terraform"` we will get the following output: `{"message":"Hello, Terraform!"}`
