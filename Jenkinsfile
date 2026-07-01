pipeline {
    agent any

    environment {
        IMAGE_NAME = 'app-devops'
        CONTAINER_NAME = 'app-devops-container'
        APP_PORT = '8082'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh "docker build -f docker/Dockerfile -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ./app"
            }
        }

        stage('Test') {
            steps {
                sh """
                    docker run -d --name test-${BUILD_NUMBER} -p 9090:80 ${IMAGE_NAME}:latest
                    sleep 3
                    curl -f http://localhost:9090/health || (docker logs test-${BUILD_NUMBER} && exit 1)
                    docker stop test-${BUILD_NUMBER}
                    docker rm test-${BUILD_NUMBER}
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:80 --restart unless-stopped ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Cleanup') {
            steps {
                sh "docker image prune -f"
            }
        }
    }

    post {
        success {
            echo "Déploiement réussi : application disponible sur le port ${APP_PORT}, via Nginx sur le port 80."
        }
        failure {
            echo "Le pipeline a échoué - voir les logs ci-dessus."
        }
    }
}