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

    # Send SNS Notification
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:042776340314:MyTopic',
        Message=f'Docker Image {image_tag} pushed at {timestamp}',
        Subject='ECR Push Notification'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Success')
    }