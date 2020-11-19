import sqlite3


class typeForSQL:
    CHAR = " char"
    TEXT = " text"
    AI = " integer primary key autoincrement"
    INT = " integer"
    NOT_NULL = " not null"


class MySQLite:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)

    def createTable(self, tableName, dictField):
        try:
            self.conn.execute('drop table if exists \'{}\';'.format(tableName))
            newList = []
            for (K, V) in dictField.items():
                newList.append("{} {}".format(K, V))
            field = ",".join(newList)
            self.conn.execute('create table {}({});'.format(tableName, field))
            return True
        except:
            return False

    def cleanTable(self, tableName):
        try:
            self.conn.execute('delete from {};'.format(tableName))
            self.conn.execute('delete from sqlite_sequence WHERE name = \'{}\';'.format(tableName))
            return True
        except:
            return False

    def insertData(self, tableName, dictData):
        try:
            field = ",".join(dictData.keys())
            value = "\'"+"\',\'".join(dictData.values())+"\'"
            self.conn.execute('insert into {}({}) values ({});'
                              .format(tableName, field, value))
            return True
        except:
            return False

    def getAllData(self, tableName, tableField="*"):
        try:
            return self.conn.execute('select {} from {};'
                                     .format(tableField, tableName))
        except:
            return False

    def commit(self):
        try:
            change = self.conn.total_changes
            self.conn.commit()
            return change
        except:
            return False

    def __del__(self):
        self.conn.close()
