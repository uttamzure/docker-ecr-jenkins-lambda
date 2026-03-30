pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REPO = "042776340314.dkr.ecr.us-east-1.amazonaws.com/myapp"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/uttamzure/docker-ecr-jenkins-lambda.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag myapp:latest $ECR_REPO:latest'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin 042776340314.dkr.ecr.us-east-1.amazonaws.com
                docker push $ECR_REPO:latest
                '''
            }
        }

        stage('Trigger Lambda') {
            steps {
                sh 'aws lambda invoke --function-name myLambdaFunction output.txt'
            }
        }
    }
}