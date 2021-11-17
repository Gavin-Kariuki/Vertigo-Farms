export MAIL_USERNAME='yourEmail@domainName.com' # change to your liking, though it is not a must you have this here.

#This is important once you clone the repo to automate the process of running start.sh
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py server --port 8888 #you can change the port number to your liking.