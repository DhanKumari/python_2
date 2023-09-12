#even no. 

"""for i in range(1,21):
    if i%2==0:
        print(i,end=" ")"""












#factorial of a no. 
"""
num=int(input("enter a no. "))
fact=1
i=1

while i<=num:
    fact =fact*i
    i+=1
print("factorial of {} is {} ".format(num,fact))
"""






#tables
"""
n=int(input("enter a no. whose multiplication table you want to print:  "))

for i in range(1,11):
    sum=i*n
    print("{} * {} = {}".format(n,i,sum))"""
   









#sum of digits of a no. 
"""
n=int(input("enter a no. "))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10

print("sum of digit  is {}".format(sum))"""










#fibonacci no.
"""
a=0
b=1
for i in range(10):
    c=a+b
    print(c)
    a=b
    b=c"""




#fibonacci no.
"""
a=0
b=1
c=0
for i in range(10):
    print(a)
    c=a
    a=b
    b=a+c"""





#prime no.  
"""

n=int(input("enter a no."))
if n==1:
    print("{} is not a prime no.".format(n))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("{} is not a prime no.".format(n))
            break
    else:
        print("{} is a prime no.".format(n))"""







"""
string=input("enter a string: ")
for i in range(len(string)-1,-1,-1):
    print(string[i],end="")
    """










"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")"""

"""
n=int(input("enter a pasitive no."))
upper=100#assuming highest range
sum=0
count=0
for i in range(2,upper+1):
    for j in range(2,i):
        if i%j==0:
           
            break
    else:
        sum=sum+i
        count+=1
        if count==n:
            break


print("for the first {} prime no. the sum is {}".format(n,sum))"""





import random
ans=random.randint(1,50)
#print(ans)
guess=0
print("guess a no.")

while guess !=ans:
    guess=int(input())
    if guess== ans:
            print("correct")
            break
    else:
        if guess <ans:
            print("guess higher ")
        else:
             print("guess lower ")
