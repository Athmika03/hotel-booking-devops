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
                echo 'Running application checks...'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t hotel-booking-app:%BUILD_NUMBER% .'
            }
        }
    }
}