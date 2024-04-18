pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    parameters {
        string(name: 'GIT_REPO', defaultValue: 'https://github.com/dimuthuhippola/docker_tutorial.git', description: 'Git repository URL')
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Git branch')
        string(name: 'FILE_PATH', defaultValue: '/home/jenkins/docker_tutorial/docker-compose.yml', description: 'Path to the file to be copied')
        string(name: 'PROD_SERVER', defaultValue: 'root@194.195.121.133:/opt', description: 'Production server SSH address')
    }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {

        stage('Copy File to Production Server') {
            steps {
                script {
                     echo "Building.."
                    // Use SCP to copy the file to the production server
                    sh " sshpass -p 'vYpom2kvqcr' scp /home/jenkins/docker_tutorial/docker-compose.yml root@194.195.121.133:/opt/text.yml"
                }
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd app
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
               
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
