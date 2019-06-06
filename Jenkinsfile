pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'scp -r * root@ncc:/home/git-ncc/'
                
            }
        }
    }
}
