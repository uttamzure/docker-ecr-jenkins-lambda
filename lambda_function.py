import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

table = dynamodb.Table('ImageLogs')

def lambda_handler(event, context):

    image_tag = event.get("image", "latest")
    timestamp = str(datetime.datetime.now())

    # Save to DynamoDB
    table.put_item(
        Item={
            'image_tag': image_tag,
            'timestamp': timestamp
        }
    )

    # Send SNS Notification (Updated Format)
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:042776340314:MyTopic',
        Subject='Docker Deployment Notification',
        Message=f'''
Hello DevOps Team,

A new Docker image has been successfully pushed to Amazon ECR.

Repository Name : myapp-repo
Image Tag       : {image_tag}
Deployment Time : {timestamp}

This deployment was automatically triggered by the Jenkins CI/CD pipeline.

Best Regards,
AWS Automation
'''
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }