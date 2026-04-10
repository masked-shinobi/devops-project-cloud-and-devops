pipeline {
agent any

```
stages {

    stage('Clone') {
        steps {
            git 'https://github.com/masked-shinobi/devops-project-cloud-and-devops.git'
        }
    }

    stage('Optimization') {
        steps {
            sh 'python3 optimizer.py'
        }
    }

    stage('Build Image') {
        steps {
            sh 'docker build -t sanjay98438/my-cloud-app:latest .'
        }
    }

    stage('Push Image') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-creds',
                usernameVariable: 'USERNAME',
                passwordVariable: 'PASSWORD'
            )]) {
                sh '''
                echo $PASSWORD | docker login -u $USERNAME --password-stdin
                docker push sanjay98438/my-cloud-app:latest
                '''
            }
        }
    }
}
```

}
