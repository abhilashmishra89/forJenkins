pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sshpass -f password scp -r -o StrictHostKeyChecking=no sipstatus.py check* readme.md  root@192.168.188.130:/home/ncc/'
                sh 'sshpass  -f password scp -o strictHostKeyChecking=no mailer.sh message.html root@192.168.188.130:/tmp/'
                sh 'sshpass -f password  ssh -o strictHostKeyChecking=no root@192.168.188.130 "/bin/sh /tmp/mailer.sh" '
            }
        }
    }
}
