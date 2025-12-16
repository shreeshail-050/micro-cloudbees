pipeline {
    agent { label 'windows' }

    stages {

        stage('Verify Repository') {
            steps {
                bat 'echo Repository cloned successfully'
                bat 'dir'
            }
        }

        stage('Backend Setup') {
            steps {
                bat '''
                cd backend
                python -m venv venv
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Frontend Setup') {
            steps {
                bat '''
                cd frontend
                python -m venv venv
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }
    }
}
