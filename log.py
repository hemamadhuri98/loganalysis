import psycopg2

def fav_articles():
    sql = """select title, count(title) as views
            from articles, log
            where log.path = concat('/article/', articles.slug)
            group by articles.title
            order by views desc
            limit 3;"""

    first_three = cal(sql)

    print('"""Top three articles in the data"""')
    for a in first_three:
        print('-> *' + a[0] + '* :: ' + str(a[1]) + "views")

def top_authors():
    sql="""
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

    print('\n ***top three authors***')
    l = 1
    for b in result:
        print('* ' + b[0] + ' :: ' + str(b[1]) + "views")
        l += 1

def dayerrors():

    sql="""
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

    print('\n"""Days with more than 1% errors"""')
    for c in result:
        print(c[0].strftime('%d %B %Y') + " : " +
              str(round(c[1]*100, 1)) + "%" + " errors")
        
def cal(sql):
   
    try:
        db = psycopg2.connect(dbname = "news")
        c = db.cursor()
        c.execute(sql)
        car = c.fetchall()
        db.close()
        return car
    except Exception:
        print("Database is unable to connect")

if __name__ == '__main__':
    fav_articles()
    top_authors()
    dayerrors()
