from pprint import pprint
import time
import myFile

log = []

# verfiy input -0 no check -1 check null -2 check float


def chkInput(displayMsg, checkMode=0):
    isUseful = False
    inp = input(displayMsg)
    while checkMode != 0 and not isUseful:
        if checkMode == 1:
            while inp == "":
                print("-----!!!不能為空值，請重新輸入!!!-----")
                inp = input(displayMsg)
        elif checkMode == 2:
            isFloat = False
            while not isFloat:
                try:
                    inp = float(inp)
                    isFloat = True
                except ValueError:
                    print("-----!!!輸入錯誤，請重新輸入!!!-----")
                    inp = input(displayMsg)
        isUseful = True
    return inp


def login(acc, psw):
    dictUserDetail = {}
    lst = myFile.readFile(['role', 'acc', 'psw'], "accounts.txt")
    for row in lst:
        if row['acc'] == acc and row['psw'] == psw:
            dictUserDetail = {"acc": row['acc'], "role": row['role'].lower()}
            break
    return dictUserDetail


def feature(userDetail):
    userLavel = userDetail['role']
    userAcc = userDetail['acc']
    log.append(logFormat(userAcc, "登入"))
    lstFeature = ["1. BMI計算", "2. 最佳體重計算"] if userLavel == "user" else [
        "1. BMI計算", "2. 最佳體重計算", "9. 查看log"]
    print("\n請輸入您想執行的功能，直接Enter則重新登入")
    print(*lstFeature, sep="\n")
    choseMode = chkInput(">>>")
    while choseMode != "":
        if choseMode == "1":
            log.append(logFormat(userAcc, "BMI計算"))
            height = chkInput(">>>身高(cm)：", checkMode=2)
            weight = chkInput(">>>體重(kg)：", checkMode=2)
            print("您的BMI指數為：{0:>.2f}".format(weight/pow(height/100, 2)))
        elif choseMode == "2":
            log.append(logFormat(userAcc, "最佳體重計算"))
            height = chkInput(">>>身高(cm)：", checkMode=2)
            print("您的最佳體重為：{0:>.2f}".format(22 * pow(height / 100, 2)))
        elif choseMode == "9" and userLavel == 'admin':
            log.append(logFormat(userAcc, "查看log"))
            readLog(log)
        print("\n請輸入您想執行的功能，直接Enter則重新登入")
        print(*lstFeature, sep="\n")
        choseMode = chkInput(">>>")
    log.append(logFormat(userAcc, "登出"))


def logFormat(user, msg):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return {"username": user, "datetime": t, "action": msg}


def writeLog(*writeMsg):
    logFile = "{0}.log".format(time.strftime("%m%d%H%M", time.localtime()))
    for dic in writeMsg:
        myFile.writeFile(logFile, "{0},{1},{2}\n".format(*dic.values()))


def readLog(logContent):
    # lstLogFile = myFile.readFolder("./",".log")
    # logContent=[]
    # if len(lstLogFile) > 0:
    #     for logfile in lstLogFile:
    #         logContent.extend(myFile.readFile(
    #             ['username', 'datetime', 'action'], logfile))
    pprint(logContent if len(logContent) > 0 else "讀取失敗", depth=3)


# execute
isExit = False
print("\n請輸入帳密進行登入，直接Enter則離開")
uid = chkInput(">>>帳號：")
while uid != "":
    psw = chkInput(">>>密碼：", checkMode=1)
    userDetail = login(uid, psw)
    # print(userDetail)   # display user acc/role
    feature(userDetail) if len(userDetail) > 0 else print("帳號或密碼錯誤")
    print("\n請輸入帳密進行登入，直接Enter則離開")
    uid = chkInput(">>>帳號：")
writeLog(*log)
print("再見!")
