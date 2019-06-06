pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'scp .* ncc:/home/git-ncc/'
                
            }
        }
    }
}
