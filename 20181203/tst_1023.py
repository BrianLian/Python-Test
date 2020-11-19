
# 宣告使用 sqlite3 模組
import sqlite3

# 建立對檔案型資料庫 mydb.db 的物件參考


conn = sqlite3.connect('mydb.db')

conn.execute("drop table if exists member")
# 建立資料表
conn.execute('''
    create table member
    (
        iid  integer primary key autoincrement,
        mid     char(8)             not null,
        mname   text                not null,
        mpass   char(32)            not null
    );
''')


# 新增紀錄
conn.execute('''
    insert into member(mid, mname, mpass) values ('99103642', 'Janet', '851022');
''')
conn.execute('''
    insert into member(mid, mname,mpass) values ('99103643', 'Tom', 'IamGenuis');
''')

# 修改紀錄
conn.execute('''
    update member set mpass='123456' where mid='99103642';
''' )

# 查詢
cursor = conn.execute('''
    select * from member;
''')
for record in cursor:
    print("id={}".format(record[0]))
    print("name={}".format(record[1]))
    print("password={}".format(record[2]))
    print("password={}".format(record[3]))
    print()

# 刪除紀錄
conn.execute('''
    delete from member where mname='Tom';
''')

# 將變動寫入檔案
conn.commit()
print("change {} records".format(conn.total_changes))

# 關閉連線物件
conn.close()
