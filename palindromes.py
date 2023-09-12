
def multiply(x:float, y:float)->float:
    result=x*y
    return result


def is_palindrome(string:str)-> bool:
     return string[::-1].casefold()==string.casefold()
     """back=a[::-1]#reverse the string 
     return back==a #check if they are equal 

"""


def pal_sen(sentence:str)-> bool:
    string="" #empty string 
    for char in sentence:
        if char.isalnum():
               string+=char
    print(string)
    #return string[::-1].casefold()==string.casefold()
    return is_palindrome(string)
               

"""
word= input("please eneter the word ")
if pal_sen(word):
     print("{} is a palindrome ".format(word))
else:
     print("{} is not a palindrome ".format(word))
"""

ans= multiply(2,5)
print(ans)

#using functions 
def fibonacci(n:int)->int: #it takes int and rreturns int 
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



p = pal_sen()
