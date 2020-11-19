a_integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a_integer_tuple = (0, 1, 2, 3, 4, 5, 6)

print("類似C#的foreach", end=" :")
for value in a_integer_list:
    print("{}{:2}".format(" ", value), end="")
print("\r\n")

print("for迴圈印出list並更改數值", end=" :")
for index in range(len(a_integer_list)):
    if index == 2:
        a_integer_list[index] = 99999
    print("{}{:2}".format("" if index == 0 else ",",
                          a_integer_list[index]), end="")
print("\r\n")

print("for迴圈印出tuple並更改數值(有錯誤 因為tuple設定後不能更改)", end=" :")
for index in range(len(a_integer_tuple)):
    # 錯誤
    # if index==2:
        # a_integer_tuple[index]="更改"
    print("{}{:2}".format(""if index == 0 else ",",
                          a_integer_tuple[index]), end="")
print("\r\n")

print("指定位置 : {} --> {}".format(2, a_integer_list[2]))
print("指定範圍 : {} --> {}".format("0~(5-1)", a_integer_tuple[0:5]))
print("\r\n")

print("原list : ", end="")
for value in a_integer_list:
    print("{}".format(value), end=" ")
print("\r\n")

a_integer_list.reverse()
print("反轉後list : ", end="")
for value in a_integer_list:
    print("{}".format(value), end=" ")
print("\r\n")

a_integer_list.sort()
print("排序後list : ", end="")
for value in a_integer_list:
    print("{}".format(value), end=" ")
print("\r\n")


a_integer_list.pop()
print("刪除最後一個元素後list : ", end="")
for value in a_integer_list:
    print("{}".format(value), end=" ")
print("\r\n")

a_integer_list.pop(1)
print("刪除編號為1的元素後list : ", end="")
for value in a_integer_list:
    print("{}".format(value), end=" ")
print("\r\n")
