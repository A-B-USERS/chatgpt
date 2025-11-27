pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mlops-app"
        APP_PORT = "8000"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/A-B-USERS/chatgpt.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 model/train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Stop and remove old container if exists
                    def containerExists = sh(script: "docker ps -a --format '{{.Names}}' | grep -w $DOCKER_IMAGE || true", returnStdout: true).trim()
                    if (containerExists) {
                        sh "docker rm -f $DOCKER_IMAGE"
                    }
                    // Run new container
                    sh "docker run -d -p $APP_PORT:8000 --name $DOCKER_IMAGE $DOCKER_IMAGE"
                }
            }
        }

        stage('Example Script Stage') {
            steps {
                script {
                    def someList = ['fastapi', 'mlops', 'docker']
                    if (someList.any { it == 'mlops' }) {
                        echo "Found 'mlops' in the list"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Everything succeeded!'
        }
        failure {
            echo 'Something failed, check logs.'
        }
    }
}
