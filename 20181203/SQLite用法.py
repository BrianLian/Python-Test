from MySQLite import *

tableName = "test"

sql = MySQLite("mydb.db")
sql.createTable(tableName, {
    "iid": typeForSQL.ai,
    "mid": typeForSQL.int,
    "mname": typeForSQL.txt+typeForSQL.not_null,
    "mpass": typeForSQL.txt
})

sql.insertData(tableName, {
    "mid": "9a417018",
    "mname": "Ian",
    "mpass": "851022"
})

allData = sql.getAllData(tableName)

for row in allData:
    rowData = []
    for data in row:
        rowData.append(data)
print(*rowData)

print("change {} records".format(sql.commit()))

sql = None
