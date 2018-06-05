# etherpad_django

To start the project follow the steps below:

1. Creation of database:

a. sudo apt-get install mysql-server
b. mysql -u root -p
c. create database etherpad_lite_db;
d. use etherpad_lite_db;

2. Making migrations

python manage.py syncdb

3. Running the server

python manage.py runserver

4. Running node application

cd etherpadproject/etherpad-lite/ 
bin/run.sh

5. Open the browser and goto localhost:8000/

