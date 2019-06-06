pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sshpass -p "jenkins" scp -r -o StrictHostKeyChecking=no * jenkins@192.168.188.130:/home/git-ncc/'
                
            }
        }
    }
}
