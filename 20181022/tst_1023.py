def bmi(height, weight, isround=True):
    return round(weight/(height/100)**2) if isround else weight/(height/100)**2


def mysum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
