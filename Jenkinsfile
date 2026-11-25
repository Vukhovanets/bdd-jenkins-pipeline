pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vukhovanets/bdd-jenkins-pipeline.git'
            }
        }

        stage('Static Code Analysis') {
            steps {
                sh '''
                    pip install pylint --break-system-packages
                    python3 -m pylint --disable=C,R features/ pages/
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run UI Tests') {
            steps {
                sh 'python3 -m behave -f allure_behave.formatter:AllureFormatter -o allure-results'
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
        }
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
