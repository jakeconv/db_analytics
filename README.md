# News Database Analytics Program (Project 1)

## About
This program will return the top 3 articles and their views, the top authors and their total article views, and the date(s) in which the total number of requests returned with an error was greater than 1%.

## Prerequisites

This program runs in Python 3.  Python may be downloaded from:

https://www.python.org/downloads/

To install, run the downloaded executable. 

For this project, the program executes within a virtual machine running on VirtualBox.  VirtualBox may be downlaoded from:

https://www.virtualbox.org/wiki/Downloads

To install, downlaod the appropriate package for your platform and run the executable.

This program was tested from within a Vagrant virtual machine environment.  A Vagrant installation package may be downloaded from:

https://www.vagrantup.com/downloads.html

Finally, this program makes use of the psycopg2 library.  To install, run the following command:

		sudo pip install psycopg2

This project utilizes data from a PostgreSQL database, which can be downloaded from here:

https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Extract the contents of the above zip file into a directory within the Vagrant virtual environment, such as the shared vagrant folder.  

## Installing
To get started, navigate to your vagrant directory.  Run the following command:

		vagrant up

Then, connect to the vagrant VM:
		
		vagrant ssh

Navigate to the directory where the newsdata.sql file was extracted to.  Run this to create the database:
		
		psql -d news -f newsdata.sql

Now, the code is ready to run.

## Views
The queries in this program are supported by the following two views.  These views must be created in the PostgreSQL before running the program.
Connect to the database using the following:

		psql -d news

Then, run the following queries.

'articleHits' view:

		create view articleHits as select a.name, b.title, count(c.path) as hits from authors as a, articles as b, log as c where c.path like concat('/article/', b.slug) and b.author = a.id group by a.name, b.title order by hits desc;

'requests' view:

		create view requests as select date(time) as date, count(*) as total, count(case when status != '200 OK' then 1 end) as bad from log group by date;

## Running
To run the database analytics, use the following command:

		python db_analytics.py

The results of the queries will be printed to the terminal.