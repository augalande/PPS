def sqroot(x):
    a=(x**(1/2))
    return a
def sq(x):
    b=x**2
    return b
def cub(x):
    c=x**3
    return c
def prime(x):
    count=0
    for i in range(1,x+1):
        if(x%i==0):
            count+=1
    if (count==2):
        return 0 #Prime Number
    else:
        return 1 #Not Prime Number
def fact(x):
    if(x==0):
        return 1
    else:
        prod=1
        for i in range (2,x+1):
            prod=prod*i
        return prod
def primefact(x):
    l1=[1]
    for i in range(1,x+1):
        if(x%i==0 and prime(i)==0):
            l1.append(i)
    return l1
x=int(input('Enter a number='))
print("Square Root of number=",sqroot(x))
print("Square of number=",sq(x))
print("Cube of number=",cub(x))
if(prime(x)==0):
    print(x,"is a Prime number")
else:
    print(x,"is not a Prime Number")
print("Factorial of number=",fact(x))
print ("Prime Factors of number=",primefact(x))