def Fn(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return Fn(n-1) + Fn(n-2)


n = 2
print('Input:{}, Output:{}'.format(n, Fn(n)))


n = 9
print('Input:{}, Output:{}'.format(n, Fn(n)))


def try_parse_int(str_val):
    try:
        return int(str_val)
    except:
        return None


while True:
    print('\n\ninput a number to calc Fib.\nInput \'exit\' will exit the process.')
    n = input('>>>n=')
    if n == 'exit':
        break
    n = try_parse_int(n)
    if n == None:
        print('please input a number.')
    else:
        print('Fn({})={}'.format(n, Fn(n)))