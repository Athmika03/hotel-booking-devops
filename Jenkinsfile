
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
                bat 'python -m unittest test_app -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t hotel-booking-app:%BUILD_NUMBER% .'
            }
        }
    }
}