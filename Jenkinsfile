pipeline {
    agent {
      label 'host'
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Build') {
            steps {
                sh " sudo docker-compose build"
            }
        }
        stage('Test') {
            steps {
                sh "sudo docker run aquasec/trivy image zemli777/weather_app:latest"
                }
        }
        stage('Deploy') {
            steps {
                sh "sudo docker-compose up"
            }
        }
    }
}