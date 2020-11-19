def check_overlapping(time1, time2):
    '''確認兩條時間線是否重疊'''
    if time1[0] > time2[1] or time1[1] < time2[0]:
        return False
    return True

def maximum_of_visitors(schedule, certain_time):
    cnts = []
    visitors = []

    # 從行程表取出在時間區間內的訪問者時間
    for time in schedule:
        if(check_overlapping(certain_time, time)):
            visitors.append(time)

    # 判斷訪問者時間與時間之間的重疊次數
    for i in range(len(visitors)):
        cnt = 0
        for j in range(i, len(visitors)):
            if(check_overlapping(visitors[i], visitors[j])):
                cnt += 1
        cnts.append(cnt)

    return max(cnts)


schedule = [
    [0, 1],
    [1.5, 2],
    [1.5, 3],
    [2, 4],
    [2, 6],
    [3, 4],
    [3.5, 4],
    [5, 5.5],
]

certain_time = [0, 1.5]
print('在{}時間段的最高人數為: {}'.format(certain_time, maximum_of_visitors(schedule, certain_time)))

certain_time = [3, 4]
print('在{}時間段的最高人數為: {}'.format(certain_time, maximum_of_visitors(schedule, certain_time)))

certain_time = [4.1, 5]
print('在{}時間段的最高人數為: {}'.format(certain_time, maximum_of_visitors(schedule, certain_time)))

certain_time = [2.1, 2.5]
print('在{}時間段的最高人數為: {}'.format(certain_time, maximum_of_visitors(schedule, certain_time)))

