pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/nothing015/ETLTestAutomation.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest pandas'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'py.test ETLTestingAutomation.py -v -s'
            }
        }
    }
    post {
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
