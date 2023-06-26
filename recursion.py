def step(x,n):
    if n == 0:
        return 1
    else:
        return x*step(x,n-1)
print(step(5,3))





def find(x):
    start =
    stop =
    mid = stop // start

    def find(x):
        min_value = min(ar)
        max_value = max(ar)
        start = ar.index(min_value)
        stop = ar.index(max_value)
        mid = (start + stop) // 2
        print(mid)
        if mid < x:
            stop = (mid - 1)
        elif mid > x:
            stop = (mid + 1)
        else:
            x = mid
            print(mid)
            return find(x)

    print(find(20))