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
  ###### -Then database connection
  ###### -I used try except approach all over the python program
  ###### -Create cursor object
  ###### -Then after creating and select queries I fetched the data with this c object
  ###### -Then close connections
## To run:
  #### -In vagrant path run command
  ###### **python log.py

