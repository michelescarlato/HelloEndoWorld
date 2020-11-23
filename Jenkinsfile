pipeline{
    agent any
    environment{
        MY_FILE = fileExists 'HelloEndoWorld'
    }
    stages{
        stage('conditional if not exists'){
            when { expression { MY_FILE == 'false' } }
            steps {
                echo "file does not exist"
                sh 'git clone https://github.com/michelescarlato/HelloEndoWorld.git'
                dir("HelloEndoWorld") {
                    sh 'pwd'
                    sh 'ls -lah'
                    sh 'make'
                    sh 'python3 server.py'
                }
            }
        }
        stage('conditional if exists'){
            when { expression { MY_FILE == 'true' } }
            steps {
                echo "file exists"
                dir("HelloEndoWorld") {
                    sh 'pwd'
                    sh 'ls -lah'
                    sh 'make'
                    sh 'python3 server.py &'
                    sh 'curl http://localhost:8079/helloworld'
                    sh 'curl http://localhost:8079/helloworld/LucianoDaSilva'
                    sh 'curl http://localhost:8079/versionz'
                    sh 'pkill python3'
                }
            }
        }
    }
}
