# Patent-Office

CSE202: Fundamentals of Database Management Systems

Capstone Project

## Team Members:
1. Aditya Singh
2. Bhavya Chopra
3. Naman Tyagi
4. Siddharth Sadhwani
5. Yashdeep Prasad

## PatentDB: Application and Domain
PatentDB is a DBMS for a patent office having multiple branches across different cities. The database caters to the operational needs of the patent office, such as office records, registered attorneys, employee and officer records, application records, as well as royalty agreement records. 

The database also allows individuals and companies to apply for patenting their innovations etc, and also for the renewal of expired patents. We also offer the following novel features:

 - Allowing patent officers to easily keep track of application examination status and providing facility to save remarks.
 - Allowing users with different roles to directly access their personalized dashboards with specific features on the basis of their role.
 - Allowing patentees and applicants to connect with their patent attorneys and vice versa
 - Building three interfaces: Command line interface, Web application interface and Mobile application interface to enable users to use any interface as per their convenience. The idea is similar to GitHub, where changes made via any application shall update the database and thus, changes shall reflect everywhere.
 
 ## Stakeholders Involved:
  - Companies and Individuals filing patents
  - Researchers, Innovators and Organisations
  - Lawyers(Patent Attorneys)
  - Patent Officers and Examiners
  - Government
  - Patentees
  - Partners (for Royalties)
  
  ## The Patent Database and it’s Relations:
  - Patent_Offices
  - Patents
  - Expired_Patents
  - Renewal_Applications
  - Company_Applicants
  - Individual_Applicants
  - Patent_Applications
  - Patentees
  - Patent_Examiner
  - Patent_Attorney
  - Royalties
  - Partners
  
  ## UML Representation for Schema and Relations:
  
  ![UML Representation for PatentDB](https://github.com/BhavyaC16/Patent-Office/blob/master/UML_Schema.png)
  
  ## Entity-Relationship Diagram:
  
  ![ER Diagram for PatentDB](https://github.com/BhavyaC16/Patent-Office/blob/master/ER_Diagram.jpg)
  

Further, PatentDB is normalised upto the BCNF level, and all queries have been optimised by careful identification and creation of indices.


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
  - Finally, cd into `Patent-Office/PatentDB` and run `python3 patentdb.py` for the command line interface, and `python3 db.py` to access the flask based web application on localhost.
  
  ## Flutter Project
  https://github.com/aditya18378/Patent-Office
  
  ## Resources
  
   - https://opensource.com/article/18/4/flask
   - https://codeburst.io/flask-for-dummies-a-beginners-guide-to-flask-part-uno-53aec6afc5b1
