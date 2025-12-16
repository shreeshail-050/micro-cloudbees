pipeline {
    agent { label 'windows' }

    stages {

        stage('Checkout') {
            steps {
                bat 'echo Code checked out'
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

        stage('Deploy Backend') {
            steps {
                bat '''
                cd backend
                start cmd /k venv\\Scripts\\python app.py
                '''
            }
        }

        stage('Deploy Frontend') {
            steps {
                bat '''
                cd frontend
                start cmd /k venv\\Scripts\\python app.py
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'curl http://localhost:5001/api/hello'
                bat 'curl http://localhost:5000'
            }
        }
    }
}
