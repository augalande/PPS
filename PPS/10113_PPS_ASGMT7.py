s=input("Enter a String:-")
print("Length of the String is ",len(s))
def rev(x):
    revs=""
    for i in x:
        revs = i+revs
    return revs
print("Reverse string of the given string is",rev(s))
eq=(s==rev(s))
print("Equality check of two strings:-",eq)
if(eq==True):
    print("Palindrome String")
else:
    print("Not a Palindrome String")
s1=rev(s)
if (s1 in s):
    print("Substing")
else:
    print("Not a Substring")

