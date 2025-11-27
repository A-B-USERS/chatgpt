pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/A-B-USERS/chatgpt.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 model/train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f mlops-app || true'
                sh 'docker run -d -p 8000:8000 --name mlops-app mlops-app'
            }
        }

        /*
        stage('Deploy to Remote Server') {
            steps {
                sh """
                ssh root@YOUR_SERVER_IP '
                    docker pull mlops-app
                    docker rm -f mlops-app || true
                    docker run -d -p 8000:8000 mlops-app
                '
                """
            }
        }
        */
    }
}

