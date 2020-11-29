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
        stage('run PATH flag test'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'pytest tests/test_1a_path_flag.py'}
                  }
              }
        stage('run test on non-standard port'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'pytest tests/test_2a_port_flag.py'}
                  }
              }
        stage('run test on endpoints'){
            steps{
                    dir("HelloEndoWorld"){
                    sh 'pytest tests/test_3_endpoints.py'}
                  }
              }
        stage('run kubernetes job'){
          steps{
                  dir("HelloEndoWorld"){
                  sh 'sudo kubectl apply -f helloendoworld-kubernetes-job.yaml && sleep 10'
                  sh 'curl 172.17.0.4:8080/helloworld && sleep 5'
                  sh 'sudo kubectl delete job helloendoworld-job && sleep 5'}
                }
            }
        }
    }
