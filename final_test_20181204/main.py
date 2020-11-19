from MySQLite import MySQLite, typeForSQL
import requests
import bs4


def chkInput(displayMsg, checkMode=0):
    '''
        verfiy input
        \n-0 no check
        \n-1 only check null
        \n-2 check float and null
        \n-3 only check float
        \n-4 check int and null
        \n-5 only check int
    '''
    isUseful = False
    inp = input(displayMsg)
    while checkMode != 0 and not isUseful:
        if checkMode == 1:
            while inp == "":
                print("!!!---請勿留空")
                inp = input(displayMsg)
        elif checkMode == 2 or checkMode == 3:
            isFloat = False
            isCheckNull = checkMode == 2
            while not isFloat:
                try:
                    inp = float(inp)
                    isFloat = True
                except ValueError:
                    if isCheckNull and inp == "":
                        break
                    print("!!!---請輸入浮點數")
                    inp = input(displayMsg)
        elif checkMode == 4 or checkMode == 5:
            isInt = False
            isCheckNull = checkMode == 4
            while not isInt:
                try:
                    inp = int(inp)
                    isInt = True
                except ValueError:
                    if isCheckNull and inp == "":
                        break
                    print("!!!---請輸入整數")
                    inp = input(displayMsg)
        isUseful = True
    return inp


def getWebHtml(url, webSelect):
    # get request and verify status code if 200 retrun target element
    req = requests.get(url)
    if req.status_code == 200:
        try:
            return bs4.BeautifulSoup(req.text, 'html.parser').select(webSelect)
        except AttributeError:
            pass
    return False


def getSelectTarget(webHtml, webSelect):
    # get target element retrun target tag
    try:
        return webHtml.select(webSelect)
    except AttributeError:
        return False


def feature(featureSwitch):
    # all feature will in this function
    dbName = "movieList.db"
    tableName = "films"
    if featureSwitch == '1':
        url = "https://movies.yahoo.com.tw/chart.html"
        targetSelect = "div.rank_list.table.rankstyle1 > div.tr"
        webRequest = getWebHtml(url, targetSelect)
        if webRequest:
            sql = MySQLite(dbName)
            sql.createTable(tableName, {
                "filmRank": typeForSQL.TEXT+typeForSQL.NOT_NULL,
                "filmDate": typeForSQL.TEXT+typeForSQL.NOT_NULL,
                "filmRating": typeForSQL.TEXT+typeForSQL.NOT_NULL,
                "filmName": typeForSQL.TEXT+typeForSQL.NOT_NULL
            })
            for rowIndex in range(1, len(webRequest)):
                rowData = getSelectTarget(webRequest[rowIndex], "div.td")
                if rowData:
                    sql.insertData(tableName, {
                        "filmRank": rowData[0].text.strip(),
                        "filmName":
                        rowData[3].text.strip() if rowIndex > 1
                        else rowData[3].h2.text.strip(),
                        "filmDate": rowData[4].text.strip(),
                        "filmRating": rowData[6].text.strip()
                    })
            print("change {} records".format(sql.commit()))
            sql = None
        else:
            print("網址無效:", url)
    elif featureSwitch == '2':
        sql = MySQLite(dbName)
        allData = sql.getAllData(tableName)
        if allData:
            print('-' * 80)
            print("{}\t{}\t{}\t{}".format("排名", "放映日期", "推薦", "片名"))
            for row in allData:
                print("{:>3}\t{:>10}\t{:>4}\t{}".format(*row))
            print('-' * 80)
            print('-' * 80)
        else:
            print("資料庫錯誤: get table \'{}\' data error".format(tableName))
        sql = None
    elif featureSwitch == '3':
        sql = MySQLite(dbName)
        sql.cleanTable(tableName)
        print("change {} records".format(sql.commit()))
        sql = None


userInput = "default"
while userInput != "":
    print("請輸入您想執行的功能，直接Enter則離開")
    print("1. 即時擷取資料")
    print("2. 查詢電影排行")
    print("3. 清除資料")
    userInput = chkInput("=>", 0)
    feature(userInput)
    print()
