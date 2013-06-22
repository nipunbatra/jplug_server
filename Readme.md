This is the repository for jPlug server side management. 
It contains the following:

1. A script to emulate jPlug HTTP request
2. A server script to process that request and dump the record into the Database

Installation
------------

Assumptions:

* Ubuntu 12+ is being used

Installing `git`

    $ sudo apt-get install git
    $ git clone https://github.com/nipunreddevil/jplug_server.git
    $ git pull
    $ cd jplug_server

Installing `python-pip`

    $ sudo apt-get install python-pip
    $ sudo apt-get install python-setuptools

Installing `MySQL` server and client

    $ sudo apt-get install mysql-server
    $ sudo apt-get install mysql-client

You may be needed to choose the root username and password. For sake of simplicity,
you may keep the password as 'password' and the username as 'root'. (This will be 
needed later when you try to connect to the Database)

Installing `requests` for making HTTP requests

    $ sudo pip install requests

Installing `MySQLDB-Connector` for Python

    $ sudo apt-get install python-mysqldb

Installing `web.py` web server

    $ sudo pip install web.py

Creating database in MySQL (corresponding to reduced number of fields currently used for testing)

    $ mysql -u root -ppassword

    mysql> create database jplug;

    Query OK, 1 row affected (0.02 sec)

    mysql> use jplug;

	Database changed

	mysql> create table data (mac varchar(10), timestamp int, voltage float, frequency float, active_power float, reactive_power float, primary key (mac,timestamp));

	Query OK, 0 rows affected (0.27 sec)

	mysql> desc data;

    
	| Field          | Type        | Null | Key | Default | Extra |
	|----------------|-------------|------|-----|---------|-------|
	| mac            | varchar(10) | NO   | PRI |         |       |
	| timestamp      | int(11)     | NO   | PRI | 0       |       |
	| voltage        | float       | YES  |     | NULL    |       |
	| frequency      | float       | YES  |     | NULL    |       |
	| active_power   | float       | YES  |     | NULL    |       |
	| reactive_power | float       | YES  |     | NULL    |       |
	
	6 rows in set (0.01 sec)


Running
-------

Running the simulation script. Currently it is sending data to localhost on port 9000

    $ python jplug_client_simulate.py

Running the server to accept the data.

    $ python server.py 9000






