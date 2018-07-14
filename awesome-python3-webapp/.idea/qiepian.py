"""
g = (x*x for x in range(1,10))
for i in g :
    print(i)
"""
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return done