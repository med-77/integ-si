pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/med-77/integ-si.git', branch: 'develop'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t nginx .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8083:80 --name nginx2 nginx'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Build and Deployment successful!'
        }
        failure {
            echo 'Build or Deployment failed.'
        }
    }
}
