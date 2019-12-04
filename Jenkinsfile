pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sshpass -f password20 scp -r -o StrictHostKeyChecking=no sipstatus.py checkHoliday.py root@192.168.188.130:/home/ncc/'
            }
        }
    }
}