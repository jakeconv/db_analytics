#!/usr/bin/env python3
#
# Program to product information on an articles database.

import psycopg2


def main():


    # First, open the database connection.  Throw an error if it does not work.
    try:
        db = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)

    # Part 1: the three most popular articles of all time    
    c = db.cursor()
    c.execute("select b.title, count(a.path) as num from log as a, "
              + "articles as b where a.path like concat('/article/', b.slug) "
              + "group by b.title order by num desc limit 3;")
    results = c.fetchall()
    print("Top 3 Articles: ")
    print("\"" + results[0][0] + "\" -- " + str(results[0][1]) + " views")
    print("\"" + results[1][0] + "\" -- " + str(results[1][1]) + " views")
    print("\"" + results[2][0] + "\" -- " + str(results[2][1]) + " views")

    # Part 2: the top authors of the publication
    c.execute("select name, sum(hits) as views from articleHits group by name "
              + "order by views desc;")
    results = c.fetchall()
    print("\nTop authors in database: ")
    for x in range(0, len(results)):
        print(results[x][0] + " -- " + str(results[x][1]) + " views")

    # Part 3: days where error rate was greater than 1%
    c.execute("select date, (bad::float/total)*100 as pct from requests where "
              + "(bad::float/total)*100 > 1;")
    results = c.fetchall()
    db.close()
    print("\nDays where more than 1% of requests led to errors:")
    for x in range(0, len(results)):
        print(results[x][0].strftime("%B %d, %Y") + " -- " + str(results[x][1])
              + "% errors")


if __name__ == '__main__':
    main()
