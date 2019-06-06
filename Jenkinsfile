pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'scp -r * ncc:/home/git-ncc/'
                
            }
        }
    }
}
