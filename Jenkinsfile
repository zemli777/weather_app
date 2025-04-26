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
                sudo docker-compose build
            }
        }
        stage('Test') {
            steps {
                sudo docker run aquasec/trivy image zemli777/weather_app:latest
                }
        }
        stage('Deploy') {
            steps {
                sudo docker-compose up
            }
        }
    }
}