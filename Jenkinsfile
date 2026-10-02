
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Hotel Booking application...'
            }
        }

        stage('Test') {
            steps {
                bat '''
                    "C:\\Users\\HP\\AppData\\Local\\Python\\bin\\python.exe" -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    .venv\\Scripts\\python.exe -m unittest test_app -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t hotel-booking-app:%BUILD_NUMBER% .'
            }
        }
    }
}