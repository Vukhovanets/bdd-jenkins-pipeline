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
                sh 'pip install pylint --break-system-packages'
                sh 'pylint --disable=C,R features/ pages/'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run UI Tests') {
            steps {
                script {
                    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                        sh 'behave -f allure_behave.formatter:AllureFormatter -o allure-results'
                    }
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
