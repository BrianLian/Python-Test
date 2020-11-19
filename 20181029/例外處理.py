b = True
while b:
    try:
        inp = int(input('請輸入整數:'))
        print('{0} 為 {1}'.format(inp, '奇數' if inp % 2 else '偶數'))
        b = False
    except ValueError:
        print('請輸入整數!')
    except EOFError:
        print('程式中斷')
        b = False
    except:
        print('不明程式中斷')
        b = False
print('再見~')
