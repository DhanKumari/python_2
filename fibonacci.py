"""a=0
b=1
for i in range(10):
    print(a)
    c=a
    a=b
    b=c+a"""

#using functions 
def fibonacci(n):
    """return the 'n' in fibonacci number,for positive 'n' """
    if 0<=n<=1:
        return n
    
    n_minus1,n_minus2=1,0
    result=None
    for f in range(n-1):
        result=n_minus1+n_minus2
        n_minus2=n_minus1
        n_minus1=result

    return result

for i in range(36):
    print(i,fibonacci(i))