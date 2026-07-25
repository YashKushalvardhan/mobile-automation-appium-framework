// Jenkinsfile

pipeline {
    agent any

    environment {
        // Appium server + emulator run on the Windows host, not inside
        // any container. host.docker.internal lets containers reach
        // services running on the host machine.
        APPIUM_SERVER_URL = "http://host.docker.internal:4723"

        // NOTE: Since Jenkins itself runs inside a Linux container,
        // this path must be reachable by the Appium server process,
        // which runs on the Windows host — so this stays a Windows path.
        APK_PATH = "E:\\Automation\\mobile-automation-appium-framework\\apps\\ApiDemos.apk"
    }

    stages {

        stage('Checkout') {
            steps {
                // Pulls the latest code from GitHub
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
                    docker run --rm \
                    --add-host=host.docker.internal:host-gateway \
                    -e APPIUM_SERVER_URL=$APPIUM_SERVER_URL \
                    -e APK_PATH="$APK_PATH" \
                    -v $WORKSPACE/reports:/app/reports \
                    mobile-automation-tests \
                    python -m pytest -v --alluredir=reports/allure-results
                '''
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