
def pr_prv(nane):
    """Print Privetstvie"""
    print('Congratulations, ' + nane + ' you are the best!')
    print('You very good!')

def aaa():
    print('AAAAAAA')

print('=========================')


pr_prv('vasgen')
aaa()


def sum(x,y):
    return x+y
x = sum(22,33)
print(x)
#sum(10,34)





def factorial(x):
    """Factroial number x"""
    a = 1
    ar = []
    for i in range (1,x+1):
        ar.append(i)
        i = i-1
        print(ar)
    import math
    x = math.prod(ar)
    return x
print(factorial(6))

for p in range(1,10):
    print(str(p) + '!\t = ' + str(factorial(p)))









