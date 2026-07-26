pipeline {
    agent any

    environment {
        APPIUM_SERVER_URL = "http://host.docker.internal:4723"
        APK_PATH = "E:\\Automation\\mobile-automation-appium-framework\\apps\\ApiDemos.apk"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YashKushalvardhan/mobile-automation-appium-framework.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mobile-automation-tests .'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --name mobile-tests-run \
                    --add-host=host.docker.internal:host-gateway \
                    -e APPIUM_SERVER_URL=$APPIUM_SERVER_URL \
                    -e APK_PATH="$APK_PATH" \
                    mobile-automation-tests \
                    python -m pytest -v --alluredir=reports/allure-results --reruns 2 --reruns-delay 5 || true
                '''
                // Ensure the destination directory exists before copying —
                // docker cp does not create parent directories automatically
                sh 'mkdir -p reports'
                sh 'docker cp mobile-tests-run:/app/reports/allure-results ./reports/allure-results'
                sh 'docker rm mobile-tests-run'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Check console output for test results.'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed — check logs above.'
        }
    }
}