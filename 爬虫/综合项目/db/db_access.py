import sqlite3,datetime


def insert_hisq_data(row):
    connect = sqlite3.connect(database='D:\MyProj\Course\课程资料\爬虫\综合项目\db.sqlite')
    print(row)
    # try:
    cursor = connect.cursor()
    # sql = 'insert into HistoricalQuote (HDate, Open, High, Low, Close, Volume, Symbol) values ("%s","%s","%s","%s","%s","%s","%s") '
          # 'values (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'
          # 'values (%s,%s,%s,%s,%s,%s,%s)'
    sql = 'insert into historicalquote ' \
          '(HDate,Open,High,Low,Close,Volume,Symbol)' \
          'values (:Date,:Open,:High,:Low,:Close,:Volume,:Symbol)'

    print(sql)
    count = cursor.execute(sql,row)
    print('影响行数{}'.format(count))
    connect.commit()
    # except sqlite3.DatabaseError as e:
    #     connect.rollback()
    #     print('error:',e)
    # finally:
    #     connect.close()
# insert_hisq_data((datetime.datetime(2018, 7, 17, 0, 0),'191.8', '191.78', '190.4', '189.93',  '16,365,720','appl'))