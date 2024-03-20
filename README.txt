Resources needed in your AWS account before beginning the demos:

1. An S3 bucket
    a. You can find an example of the bucket policy in the Permissions folder
2. IAM Roles for the lambda functions
    a. Policies to attach
        i. LambdaBasicExecutionRole
        ii. AWSXrayFullAccess
        iii. AmazonSSMFullAccess or more tightly scoped custom policy
        iiii. AmazonS3FullAccess or more tightly scoped custom policy
3. Parameters in AWS Systems Manager Parameter Store
    a. One parameter for the bucket name, unencrypted
        i. Use dragon_data_bucket_name for the name of the parameter
    b. One parameter for the key name, unencrypted
        i. Use dragon_data_file_name for the name of the parameter

**ARCHITECTURE FOR THE PROJECT**
![Project Architecture](https://github.com/lolawin3/dragon-sighting-serverless-app/blob/main/Architecture.png)
