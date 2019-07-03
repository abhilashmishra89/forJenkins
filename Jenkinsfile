pipeline {
    agent {
        node {
            label 'master'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sshpass -p "ips@ameyo020" scp -r -o StrictHostKeyChecking=no sipstatus1.py check* __py*  root@192.168.188.130:/home/ncc/'
                
            }
        }
    }
}
