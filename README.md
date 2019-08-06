News Database Analytics Program (Project 1)
This program will return the top 3 articles and their views, the top authors and their total article views, and the date(s) in which the total number of requests returned with an error was greater than 1%.

This program requires the psycopg2 library in order to run.

To run, use the following command:
python db_analytics.py

The queries in this program are supported by the following two views:

'articleHits' view:
create view articleHits as select a.name, b.title, count(c.path) as hits from authors as a, articles as b, log as c where c.path like concat('/article/', b.slug) and b.author = a.id group by a.name, b.title order by hits desc;

'requests' view:
create view requests as select date(time) as date, count(*) as total, count(case when status != '200 OK' then 1 end) as bad from log group by date;

In order to run correctly, these views must be created in the PostgreSQL database.