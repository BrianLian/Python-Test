import re

arrVerifyString = ["6", "-6", "606", "-606",
                   "dAkjfh", "6606aH8aA6fa", "4j3FSd中文k"]

reCheckUSNum = "^([0-9]+)$"
reCheckSNum = "^(-[0-9]+)$"
reCheckNum = "^(-[0-9]+|[0-9]+)$"
reCheckEn = "^([A-Za-z]+)$"
reCheckEnNum = "^([0-9A-Za-z]+)$"
reCheckEnNumCh = "^([0-9A-Za-z\u4e00-\u9fa5]{7,9})$"

for verifyString in arrVerifyString:
    if re.findall(reCheckUSNum, verifyString):
        print("{0} 為正整數".format(verifyString))
    if re.findall(reCheckSNum, verifyString):
        print("{0} 為負整數".format(verifyString))
    if re.findall(reCheckNum, verifyString):
        print("{0} 為整數".format(verifyString))
    if re.findall(reCheckEn, verifyString):
        print("{0} 為純英".format(verifyString))
    if re.findall(reCheckEnNum, verifyString):
        print("{0} 為英數組合".format(verifyString))
    if re.findall(reCheckEnNumCh, verifyString):
        print("{0} 為中英數組合".format(verifyString))
