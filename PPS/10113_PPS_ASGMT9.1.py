class EMPLOYEE:
    male=0
    female=0
    rich=0
    assnt=0
    def __init__(self,name,desig,gender,doj,sal):
        self.name=name
        self.desig=desig
        self.gender=gender
        self.doj=doj
        self.sal=sal
    def ge(self):
        if self.gender=='Male':
            EMPLOYEE.male+=1
        elif self.gender=='Female':
            EMPLOYEE.female+=1
    def re(self):
        if (self.sal>10000):
            EMPLOYEE.rich+=1
    def ae(self):
        if self.desig=='Asst Manager':
            EMPLOYEE.assnt+=1
    def print(self):
        print("Total Employee=",total)
        print("No of Male Employees=",EMPLOYEE.male)
        print("No of Female Employees=",EMPLOYEE.female)
        print("No of Employees having salary more than 10000=", EMPLOYEE.rich)
        print("No of Assistant Managers=",EMPLOYEE.assnt)
total=0
while(True):
    name = input("Enter your Name:-")
    desig = input("Enter your Designation:-")
    gender = input("Enter your Gender:-")
    doj = input("Enter your Date of Joining:-")
    sal = int(input("Enter your Salary:-"))
    e1 = EMPLOYEE(name, desig, gender, doj, sal)
    total += 1
    e1.ge()
    e1.re()
    e1.ae()
    a=(input('''    Hit 0 to continue
    Hit 1 to stop'''))
    if(a=='1'):
        break
    elif(a=='0'):
        pass
    else:
        break
e1.print()