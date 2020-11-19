def minimum_prod(arr):
    min_prod_val = None
    for val in arr:
        if val is not 0:
            min_prod_val = min_prod_val * val if min_prod_val is not None else val
    return min_prod_val if min_prod_val is not None else 0


a = [-1, -1, -2, 4, 3]
print('Output:{}'.format(minimum_prod(a)))

a = [-1, 0] 
print('Output:{}'.format(minimum_prod(a)))

a = [0, 0, 0]
print('Output:{}'.format(minimum_prod(a)))

a = [-2, -66, 33, 0]
print('Output:{}'.format(minimum_prod(a)))