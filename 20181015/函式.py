

# 計算總和
def fun_total(*nums):
    total = 0
    for x in nums:
        if type(x) == list or type(x) == tuple or type(x) == range:
            for num in x:
                total += num
        elif type(x) == int or type(x) == float:
            total += x
        else:
            pass
    return total


# 計算奇數總和
def fun_odd_total(*nums):
    total = 0
    for x in nums:
        if type(x) == list or type(x) == tuple or type(x) == range:
            for num in x:
                if num % 2 == 1:
                    total += num
        elif type(x) == int or type(x) == float:
            if x % 2 == 1:
                total += x
        else:
            pass
    return total


# 計算偶數總和
def fun_even_total(*nums):
    total = 0
    for x in nums:
        if type(x) == list or type(x) == tuple or type(x) == range:
            for num in x:
                if num % 2 == 0:
                    total += num
        elif type(x) == int or type(x) == float:
            if x % 2 == 0:
                total += x
        else:
            pass
    return total


print("0~10的總和:{}".format(
    fun_total([0, 1, 2], (3, 4, 5), 6, 7, 8, "字串", range(9, 11))))
print("0~9的總和:{}".format(fun_total(range(10))))
print("2~9的總和:{}".format(fun_total(range(2, 10))))
print("0~99加上666的總和:{}".format(fun_total(range(100), 666)))
print("0~99的偶數總和:{}".format(fun_even_total(range(100))))
print("0~99的奇數總和:{}".format(fun_odd_total(range(100))))
