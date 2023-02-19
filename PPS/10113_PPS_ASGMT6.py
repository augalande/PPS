def BintoDec(b):
    d = 0
    m = 1
    l = len(str(b))
    for i in range(l):
        rem = b % 10
        d = d + (rem * m)
        m = m * 2
        b = int(b / 10)
    return d
b=int(input("Enter the Binary Number: "))
print("Equivalent Decimal Value = ", BintoDec(b))

