n = int(input("Enter the number of terms you want in Fibonacci Series:"))
a = 0
b = 1
print()
print(a, b, end=" ")
for i in range(n - 2):
    c = a + b
    print(c, end=" ")
    a = b
    b = c