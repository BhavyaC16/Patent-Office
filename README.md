# Patent-Office
DBMS Group Project

## Setting up local environment

 - First, clone the repository:
`git clone https://github.com/BhavyaC16/Patent-Office.git`

Run the following commands:
 - Install `mysqlclient`:
`sudo apt-get install libmysqlclient-dev`
 - pip install Flask-MySQLDB framework:
 `pip install flask-mysqldb`
 - Run mysql and type in the following commands:
 ```sql
 create database test;
 use test;
 CREATE TABLE MyUsers ( firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL);
 ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin';
 ```
  - Finally, cd into the repository and run `python3 test.py`
