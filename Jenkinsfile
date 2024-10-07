pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests
                    bat 'python -m unittest discover tests'
                }
            }
        }
        stage('Run Server') {
            steps {
                script {
                    // Run the Flask server
                    bat 'python app/server.py'
                }
            }
        }
    }
}
