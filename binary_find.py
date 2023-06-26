ar = [33,42,51,57,68,70,77,79,81,10,12,13,15,20,24,27,] #15  если мид находится "дальше" чем искомое число, нужно отрезать ( элемент массива с индексом мид) то нужно
                                                       # мид = стоп-1, если же мид меньше чем искомое число, то нужно старт +1
ar.sort()
print(ar)

min_value = min(ar)
max_value = max(ar)
start = ar.index(min_value)
stop = ar.index(max_value)
mid = (start+stop) // 2

def find(x):
    global mid, stop, start, max_value, min_value, ar
    if x not in ar:
        print('Error input')
        exit()
    if ar[mid] > x:
        stop = (mid - 1)
        mid = (start + stop) // 2
        return find(x)
    elif ar[mid] < x:
        start = (mid + 1)
        mid = (start+stop) // 2
        return find(x)
    else:
        return mid
print(ar)
print(find(20))
