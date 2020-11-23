pipeline{
    agent any
    environment{
        MY_FILE = fileExists 'HelloEndoWorld'
    }
    stages{
        stage('Fetch and Compile: if repo do not exists'){
            when { expression { MY_FILE == 'false' } }
            steps {
                echo "file does not exist"
                sh 'git clone https://github.com/michelescarlato/HelloEndoWorld.git'
                dir("HelloEndoWorld") {
                    sh 'pwd'
                    sh 'ls -lah'
                    sh 'make'
                }
            }
        }
        stage('Fetch and Compile:if repo exists'){
            when { expression { MY_FILE == 'true' } }
            steps {
                echo "file exists"
                dir("HelloEndoWorld") {
                    sh 'pwd'
                    sh 'ls -lah'
                    sh 'git fetch'
                    sh 'git reset --hard HEAD'
                    sh 'git merge "@{u}"'
                    sh 'make'
                  }
                }
              }
        stage('run HTTP server'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'python3 server.py &'}
                  }
                }
        stage('run test on standard port'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'python3 -m pytest'}
                  }
                }
        stage('Kill the server'){
            steps{
                    sh 'pkill python3'
                  }
                }
        stage('run HTTP server on different port'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'python3 server.py -p 7077 &'}
                  }
                }
        stage('run test on different port'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'python3 -m pytest'}
                  }
                }
        stage('Kill the server again'){
            steps{
                    sh 'pkill python3'
                  }
                }
            }
        }
