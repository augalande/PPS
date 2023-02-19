def rev(n2):
    rev=0
    while(n2>0):
        a=n2%10
        rev=rev*10+a
        n2=n2//10
    return rev
n1=int(input("Enter a Number:-"))
n3=rev(n1)
print("Reverse of the entered number:-",n3)
