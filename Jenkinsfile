pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'scp -r -o StrictHostKeyChecking=no * 192.168.188.130:/home/git-ncc/'
                
            }
        }
    }
}
