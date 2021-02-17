def factorial(n,a):
    if n==0:
        return a
    else:
        return factorial(n-1,a*n)

def fibbo(n,a,b):
    if n==0 or n==1:
        return b
    else:
        return fibbo(n-1,b,a+b)

if __name__=="__main__":
    a=1
    b=1
    print(factorial(5,a))
    print(fibbo(5,b,a))