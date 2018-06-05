# etherpad_django

##To start the project follow the steps below:

1. Activate virtual environment
```
source venv/bin/activate
```
2. Creation of database:
```
a. sudo apt-get install mysql-server
b. mysql -u root -p
c. create database etherpad_lite_db;
d. use etherpad_lite_db;
```
3. Making migrations
```
python manage.py syncdb
```
4. Running the server
```
python manage.py runserver
```
5. Running node application
```
cd etherpadproject/etherpad-lite/ 
bin/run.sh
```
6. Open the browser and goto [localhost:8000](localhost:8000/)
