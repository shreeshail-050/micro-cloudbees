kpipeline {

    agent none

    stages {

        stage('Build Image') {
            agent { label 'linux' }
            steps {
                sh '''
                podman build -t docker.io/shreeshail050/todo-microservice:1.0 .
                '''
            }
        }

        stage('Push Image') {
            agent { label 'linux' }
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    podman login docker.io -u $DOCKER_USER -p $DOCKER_PASS
                    podman push docker.io/shreeshail050/todo-microservice:1.0
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            agent { label 'controller' }
            steps {
                sh '''
                kubectl apply -f todo-deployment.yaml
                kubectl apply -f todo-service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            agent { label 'controller' }
            steps {
                sh '''
                kubectl rollout status deployment/todo-app
                kubectl get pods
                '''
            }
        }
    }
}

