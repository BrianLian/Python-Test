import sqlite3


class typeForSQL:
    char = "char"
    txt = "text"
    ai = "integer primary key autoincrement"
    int = "integer"
    not_null = "not null"

class MySQLite:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)

    def createTable(self, tableName, dictField):
        self.conn.execute('drop table if exists \'{}\';'.format(tableName))
        newList = []
        for (K, V) in dictField.items():
            newList.append("{} {}".format(K, V))
        field = ",".join(newList)
        self.conn.execute('create table {}({});'.format(tableName, field))

    def insertData(self, tableName, dictData):
        field = ",".join(dictData.keys())
        value = "\'"+"\',\'".join(dictData.values())+"\'"
        self.conn.execute('insert into {}({}) values ({});' \
        .format(tableName, field, value))

    def getAllData(self, tableName, tableField="*"):
        return self.conn.execute('select {} from {};'.format(tableField, tableName))

    def commit(self):
        change = self.conn.total_changes
        self.conn.commit()
        return change

    def __del__(self):
        self.conn.close()

