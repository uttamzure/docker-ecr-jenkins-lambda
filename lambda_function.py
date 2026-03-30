import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    print("Docker Image Pushed Successfully 🚀")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed!')
    }