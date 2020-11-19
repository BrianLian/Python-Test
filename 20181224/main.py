import sqlite3
import requests
import json
from bs4 import BeautifulSoup
import json

# 建立資料庫
conn = sqlite3.connect('DataBasePM25.db')
cursor = conn.cursor()

# 建立資料表
sqlstr = '''
create table if not exists TablePM25 (
    "iid" integer primary key autoincrement not null unique,
    "SiteName" text not null,
    "MonitorDate" text not null,
    "AQI" integer,
    "PM25SubIndex" integer)
'''
cursor.execute(sqlstr)
conn.commit

url = "http://opendata.epa.gov.tw/webapi/Data/ATM00679/?$filter=MonitorDate%20eq%20%272018-12-23%27&$select=SiteName,MonitorDate,AQI,PM25SubIndex&$orderby=AQI%20desc&$skip=0&$top=1000&format=json"
html = requests.get(url)
if html.status_code != 200:
    print('網址無效:', html.url)
    quit()

soup = BeautifulSoup(html.text, 'html.parser')
jsondata = json.loads(soup.text)
# print(jsondata)

for site in jsondata:
    SiteName = site["SiteName"]
    MonitorDate = site["MonitorDate"]
    AQI = 0 if site["AQI"] == "" else int(site["AQI"])
    PM25SubIndex = 0 if site["PM25SubIndex"] == "" else int(
        site["PM25SubIndex"])
    # print(SiteName, MonitorDate, AQI, PM25SubIndex)
    sqlstr = "insert into TablePM25 (SiteName, MonitorDate, AQI, PM25SubIndex) values ('{}','{}',{},{})".format(
        SiteName, MonitorDate, AQI, PM25SubIndex)
    # print(sqlstr)
    cursor.execute(sqlstr)
    conn.commit()
conn.close()

try:
    conn = sqlite3.connect('DataBasePM25.db')
    # 查詢
    sql = "select * from TablePM25;"
    recs = conn.execute(sql)
    print('-'*60)
    print("{:2} {:8} {:3} {:30} ".format("測站目標", "監測日期", "空氣品質指標", "細懸浮微粒副指標"))
    print('-'*60)
    for rec in recs:
        print("{:>4} {:12} {:<5} {:<5} ".format(
            rec[1], rec[2], rec[3], rec[4]),  end='')
        print()
    print('-'*60)
except sqlite3.Error as e:
    print("資料庫錯誤: %s" % e)
except Exception as e:
    print("發生例外: %s" % e)
finally:
    if 'conn' in dir():
        conn.close()    # 若定義了 conn 連線物件則關閉
