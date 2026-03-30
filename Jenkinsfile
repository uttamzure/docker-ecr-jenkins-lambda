pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ACCOUNT_ID = "042776340314"
        ECR_REPO = "myapp"
        IMAGE_TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/uttamzure/docker-ecr-jenkins-lambda.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myapp:latest .'
            }
        }

        stage('Login ECR') {
            steps {
                bat "aws ecr get-login-password --region %AWS_REGION% | docker login --username AWS --password-stdin %ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com"
            }
        }

        stage('Tag Image') {
            steps {
                bat "docker tag myapp:latest %ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPO%:%IMAGE_TAG%"
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push %ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPO%:%IMAGE_TAG%"
            }
        }
    }
}