# GraphQL for [Bigbang](https://github.com/datactive/bigbang)

# Construction Instructions

## 1. Set up MySQL on MacOS
The simplest and fastest method to get MySQL running on your machine is
```bash
$ brew update && brew upgrade && brew cleanup
$ brew install mysql
```
as I have done. However, other methods to get MySQL running exist of course (such as building it yourself using the MySQL `.dmg` file which is available from the project website). To insure that the content of our database are secured and only accessible to those who have a data access permit, one has to set up a minimal security protocol via
```bash
$ mysql.server start
$ mysql_secure_installation
```
After setting up the security protocol is done, one can enter the interactive mysql environment
```bash
$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.29 Homebrew

... [more text] ...

mysql>
```
Once we successfully connected to the MySQL server we can define a simply database that is going to contain the Email data
```MySQL
mysql> CREATE DATABASE bigbang_test;
mysql> source ./mysql.txt
```
Once the data is loaded into the table, we can inspect it, e.g., using some basic MySQL commands
```MySQL
mysql> SELECT senderAdress, dateTime, subject FROM email LIMIT 5;
mysql> SELECT COUNT(*) FROM email;
```
Following the steps outlined above can of course result in various errors. To foresee some of them, I advice skimming through 'Learning MySQL: Get a Handle on Your Data' by  Vinicius M. Grippa and Sergey Kuzmichev.

When you are finished with your MySQL session don't forget to close the connection variable
```bash
$ mysql.server stop
```


## 2. Set up Server and Client for GraphQL using Python

GraphQL is a query language for APIs where client requests (query) data from a server, or requests the server to update data (mutation) on a server. In order to facilitate the exchange between a client and server we use the following Python packages
```bash
$ pip install flask ariadne flask-sqlalchemy flask-cors
```
After the Python packages are installed, we need to tell Flask which file contains our application and that we are in development stage (thus switch on Verbose mode)
```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```
Once these environment variables are declared, we can run our application
```bash
$ python app.py
 * Serving Flask app 'bigbangGraphQL.api' (lazy loading)
 * Environment: production
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```
In the last step we can type into your browser search bar `http://127.0.0.1:5000/graphql`, which will bring you to the Apollo GraphQL query builder environment. In this environment, you can test your API and create queries that you will use later in other applications.
