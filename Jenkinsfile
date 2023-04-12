
pipeline {
    agent any
    stages {
         stage('Update Git Repo'){
            steps {
                sh '''
                    #!/bin/sh
                    echo 'Pulling down changes from Github'

                    cd /usr/local/bin/django/portfolioNV
                    sudo git pull

                    echo 'Git Repo has been updated'
                    '''
            }
        }        
         stage('Update Python Virtual Environment'){
            steps {
                sh '''
                    #!/bin/sh
                    echo 'Updating Python Dependancies'

                    source /usr/local/bin/django/venv/bin/activate

                    pip install -r /usr/local/bin/django/portfolioNV/requirements.txt

                    echo 'Python Dependancies have been updated'
                    
                    '''
            }
        }
        stage('Update Django'){
            steps {
                sh '''
                    #!/bin/sh
                    echo 'Collecting static'

                    source /usr/local/bin/django/venv/bin/activate

                    cd /usr/local/bin/django/portfolioNV

                    python manage.py collectstatic --noinput

                    echo 'Django application has been updated'

                    '''
            }
        }
        stage('Redeploy Servers'){
            steps {
                sh '''
                    #!/bin/sh

                    echo 'Performing daemon-reload'
                    sudo systemctl daemon-reload

                    echo 'Restarting Gunicorn Application Server'
                    sudo systemctl restart gunicorn
                    sudo systemctl status gunicorn

                    echo 'Restarting NGINX Web Server'
                    sudo systemctl restart nginx
                    sudo systemctl status nginx

                    '''
            }
        }        
    }
}
