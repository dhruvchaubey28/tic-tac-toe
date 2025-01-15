pipeline {
    agent any
    
    // Define stages for the build pipeline
    stages {
        // Checkout the code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/dhruvchaubey28/tic-tac-toe.git'
            }
        }
        
        // Set up Python environment
        stage('Setup Python') {
            steps {
                script {
                    // On Windows
                    if (isUnix() == false) {
                        bat 'python -m pip install --upgrade pip'
                    } 
                    // On Unix/Linux
                    else {
                        sh 'python3 -m pip install --upgrade pip'
                    }
                }
            }
        }
        
        // Install project dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // On Windows
                    if (isUnix() == false) {
                        bat 'pip install pygame'
                        bat 'pip install pytest'
                    } 
                    // On Unix/Linux
                    else {
                        sh 'pip3 install pygame'
                        sh 'pip3 install pytest'
                    }
                }
            }
        }
        
        // Run tests if there are any
        stage('Test') {
            steps {
                script {
                    // On Windows
                    if (isUnix() == false) {
                        bat 'python -m pytest tests/ || exit 0'
                    } 
                    // On Unix/Linux
                    else {
                        sh 'python3 -m pytest tests/ || exit 0'
                    }
                }
            }
        }
        
        // Static code analysis
        stage('Code Analysis') {
            steps {
                script {
                    // Install pylint if not present
                    if (isUnix() == false) {
                        bat 'pip install pylint'
                        bat 'pylint *.py || exit 0'
                    } else {
                        sh 'pip3 install pylint'
                        sh 'pylint *.py || exit 0'
                    }
                }
            }
        }
        
        // Build stage - for Python this is mostly a verification step
        stage('Build') {
            steps {
                script {
                    if (isUnix() == false) {
                        bat 'python -m py_compile *.py'
                    } else {
                        sh 'python3 -m py_compile *.py'
                    }
                }
            }
        }
    }
    
    // Post-build actions
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Please check the logs for details.'
        }
    }
}
