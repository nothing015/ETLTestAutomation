pipeline {
  agent any
  stages {
    stage('Running tests') {
      steps {
        sh 'py.test ETLTestingAutomation.py -v -s'
      }
    }
  }
}
