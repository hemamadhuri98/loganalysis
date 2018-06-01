# Log-analysis
This is the third project for the Udacity Full Stack Nanodegree. In this
project, a large database with over a million rows is explored by
building complex SQL queries to draw business conclusions for the data.
The project mimics building an internal reporting tool for a newspaper site
to discover what kind of articles the site's readers like. The database
contains newspaper articles, as well as the webserver log for the site.
## To build:
we need
-python 
-vagrant
-virtual box
-postgres
## Setup:
  Firstly,create a vagrant folder on desktop and open command prompt or
  terminal in that path
#### installation commands of vagrant
  ###### -vagrant -v
  ###### -vagrant init ubuntu/trusty64
  ###### -vagrant up
  ###### -vagrant ssh
#### Now,install postgres by a command:
  ###### -sudo apt -get install python-psycopg2
  ###### -sudo apt -get install postgresql postgresql-contrib
#### To,change to postgres folder we need to use command:
  ###### -sudo -i -u postgres
#### Then,to connect to postgres database command is:
  ###### -psql
#### Then,to display all the files in this directory command is:
  ###### -\ls
#### Then create of user with some password:
  ###### -create user vagrant with password 'vagrant'
#### To display all the roles:
  ###### -\du
#### To create different roles in the database created is:
  ###### -alter user vagrant with Superuser
  ###### -alter user vagrant with Createrole
  ###### -alter user vagrant with replication
#### To exit from one database we need to use command:
  ###### -\q or exit 
#### Now,create vagrant database:
  ###### -Createdb vagrant
#### Now,open database vagrant by:
  ###### -psql
#### Then create database named news:
  ###### -Createdb news
#### Now, to connect vagrant database to news database:
  ###### -/c news
#### To,fetch sql files we use: 
  ###### -psql -d news -f newsdata.sql
# About the python file:
#### Here, newsdata.sql is fetched to news database which mainly contains three tables:
  ###### -articles
  ###### -authors
  ###### -log
#### First question in this project is What are the most popular three articles of all time? 
  ###### -I created view named fav_articles
#### First question in this project is Who are the most popular article authors of all time?
  ###### -I created view named top_authors
#### First question in this project is On which days did more than 1% of requests lead to errors?
  ###### I created three views to find errors named dayerrors
#### For running all these queries we need to create python program and I created log.py as my python file
## In this firstly,
  ###### -import psycopg2
  ###### -I used try except approach all over the python program
  ###### -Then database connection
  ###### -Create cursor object
  ###### -Then after creating and select queries I fetched the data with this c object
  ###### -Then close connections
# To run the file:
1. Ensure the setup environment is as specified with all the required installs
2. Download the project files and ensure they are all in one folder.
3. Download the database file newsdata.sql and put in the same folder named vagrant.
4. Open the terminal from the folder.
5. Run the VM by entering the command vagrant up.
6. Access the VM by entering the command vagrant ssh.
7. Load/import the database by entering the command psql -d news -f newsdata.sql
8. Run the python file by entering the command **python log.py  

