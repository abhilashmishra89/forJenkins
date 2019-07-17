pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sshpass -f password20 scp -r -o StrictHostKeyChecking=no sipstatus.py check* mail_test.py root@192.168.188.130:/home/ncc/'
                sh 'sshpass -f password23 scp -r -o StrictHostKeyChecking=no forSandeep.py root@c023:/home/abhilash/'
            //    sh 'sshpass  -f password20 scp -o strictHostKeyChecking=no mailer.sh message.html root@192.168.188.130:/tmp/'
            //    sh 'sshpass -f password20  ssh -o strictHostKeyChecking=no root@192.168.188.130 "/bin/sh /tmp/mailer.sh" '
            }
        }
    }
}
