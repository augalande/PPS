#PreAssingment-2 Question-1
#Program to use of literals and datatypes in Python
int1=1
float1=2.0
bool1=True
char1='A'
string1="of single line string"
string2='''of
multi line
string'''
complex1=2+9j
none1=None
list1=[11,"Apple",'c',False,]
tuple1=(23,"Banana",'d',True)
dict1={13:"Cat",14:"Dog",15:False,16:23}
set1={13,14,"Apple","Car",'A'}
print('''Types of Datatypes in Python:-
1)Numeric Datatype
2)Dictionary Datatype
3)Boolean Datatype
4)Set Datatype
5)Sequence Datatype
      ''')
print("Numeric Datatype:-")
print("The literal",int1,"is of datatype",type(int1))
print("The literal",float1,"is of datatype",type(float1))
print("The literal",complex1,"is of datatype",type(complex1))
print("")
print("Dictionary Datatype:-")
print("The literal",dict1,"is of datatype",type(dict1))
print("")
print("Boolean Datatype:-")
print("The literal",bool1,"is of datatype",type(bool1))
print("")
print("Set Datatype:-")
print("The literal",set1,"is of datatype",type(set1))
print("")
print("Sequence Datatype:-")
print("The literal",string1,"is of datatype",type(string1))
print("The literal",string2,"is of datatype",type(string2))
print("The literal",list1,"is of datatype",type(list1))
print("The literal",tuple1,"is of datatype",type(tuple1))
print("")
print("Special Datatype:-")
print("The literal",none1,"is of datatype",type(none1))

#PreAssingment-2 Question-2
#Program to show use of comments and indentation
'''This is a multiline comment '''
#This is a singleline comment
a=10#Assingning value 10 to variable a
b=5#Assingning value 5 to variable b
c=a+b#Variable c stores the sum of variables a and b
    print(c)#Printing variable c and incorrect indentation

#PreAssingment-2 Question-3
#Program to show use of Arithmetic and Assignment Operators
print("Types of Arithmetic Operators in Python:-")
print('''1)Addition<+>
2)Subtraction<->
3)Multiplication<*>
4)Division</>
5)Modulus<%>
6)Exponentiation<**>
7)Floor division<//>
''')
print("Types of Assignment Operators in Python:-")
print('''1)Addition Assignment<+=>
2)Subtraction Assignment<-=>
3)Multiplication Assignment<*=>
4)Division Assignment</=>
5)Modulus Assignment<%=>
6)Exponentiation Assignment<**=>
7)Floor division Assignment<//=>
''')
a=20
b=10
print("Number1=20,Number2=10")
print("Addition of two numbers is",(a+b))
print("Subraction of two numbers is",(a-b))
print("Multiplication of two numbers is",(a*b))
print("Division of two numbers is",(a/b))
print("Modulus of two numbers is",(a%b))
print("Exponentiation of two numbers is",(a**b))
print("Floor division of two numbers is",(a//b))
print("")
a+=b
print("Addition Assignment of two numbers is",a)
a=20
b=10
a-=b
print("Subraction Assignment of two numbers is",a)
a=20
b=10
a*=b
print("Multiplication Assignment of two numbers is",a)
a=20
b=10
a/=b
print("Division Assignment of two numbers is",a)
a=20
b=10
a%=b
print("Modulus Assignment of two numbers is",a)
a=20
b=10
a**=b
print("Exponentiation Assignment of two numbers is",a)
a=20
b=10
a//=b
print("Floor division Assignment of two numbers is",a)

#PreAssingment-2 Question-4
#Program to show use of Logical and Bitwise Operators
print("Types of Logical Operators in Python:-")
print('''1)Logical And<and>
2)Logical Or<or>
3)Logical Not<not>
''')
print("Types of Bitwise Operators in Python:-")
print('''1)Bitwise And<&>
2)Bitwise Or<|>
3)Bitwise Not<~>
4)Bitwise XOR<^>
5)Bitwise Right Shift< >> >
6)Bitwise Left Shift< << >
''')
a=20
b=10
print("Number1=20,Number2=10")
print("Logical And of two numbers is",(a and b))
print("Logical Or of two numbers is",(a or b))
print("Logical Not of Number1 is",(not a))
print("")
print("Bitwise And of two numbers is",(a & b))
print("Bitwise Or of two numbers is",(a | b))
print("Bitwise Not of  Number1 is",(~a))
print("Bitwise XOR of two numbers is",(a ^ b))
print("Bitwise Right Shift of two numbers is",(a >> b))
print("Bitwise Left Shift of two numbers is",(a << b))

