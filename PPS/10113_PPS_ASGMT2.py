n=int(input("Enter number of items in list:-"))
sum1=0
l1=[]
for i in range(n):
    num=int(input("Enter Number: "))
    sum1=sum1+num
    l1.append(num)
max1=max(l1)
min1=min(l1)
average1=sum1//n
print("=======================================")
print()
print("Entered list is as follows:",l1)
print()
print("Maximum number in the list :",max1)
print()
print("Minimum number in the list :",min1)
print()
print("Sum of all the numbers in the list :",sum1)
print()
print("Average of numbers in the list :",average1)
print()
print("=======================================")


