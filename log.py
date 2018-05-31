# import Postgresql library
import psycopg2

# Query 1: What are the most popular three articles of all time?


def fav_articles():
    sql = """select title, count(title) as views
            from articles, log
            where log.path = concat('/article/', articles.slug)
            group by articles.title
            order by views desc
            limit 3;"""
    first_three = cal(sql)
    # Display output for Problem 1
    print('"""Top three articles in the data"""')
    for a in first_three:
        print('-> *' + a[0] + '* :: ' + str(a[1]) + "views")
# Problem 2: Who are the most popular article authors of all time?


def top_authors():
    # query 2: Who are the most popular article authors of all time?
    sql = """
        select authors.name, count(title) as num
        from authors
        join articles
        on authors.id = articles.author
        left join log
        on log.path like concat('/article/%', articles.slug)
        group by authors.name
        order by num desc
        limit 3;
    """
    result = cal(sql)
    # printing outputs.
    print('\n ***top three authors***')
    l = 1
    for b in result:
        print('* ' + b[0] + ' :: ' + str(b[1]) + "views")
        l += 1
# query 3: On which days did more than 1% of requests lead to errors?


def dayerrors():
    sql = """
        select total.day,
          round(((errors.error_requests*1.0) / total.requests), 3) as percent
        from (
          select date_trunc('day', time) "day", count(*) as error_requests
          from log
          where status like '404%'
          group by day
        ) as errors
        join (
          select date_trunc('day', time) "day", count(*) as requests
          from log
          group by day
          ) as total
        on total.day = errors.day
        where (round(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        order by percent desc;
    """
    result = cal(sql)
    # Display header and output for Problem 3
    print('\n"""Days with more than 1% errors"""')
    for c in result:
        print(c[0].strftime('%d %B %Y') + " : " +
              str(round(c[1]*100, 1)) + "%" + " errors")


def cal(sql):
    """cal takes a string as a parameter. It executes the sql
    and returns the output as a list of tuples."""
    try:
        db = psycopg2.connect(dbname="news")
        c = db.cursor()
        c.execute(sql)
        car = c.fetchall()
        db.close()
        return car
    except Exception:
        print("Unable to connect to the database")

if __name__ == '__main__':
    fav_articles()
    top_authors()
    dayerrors()
