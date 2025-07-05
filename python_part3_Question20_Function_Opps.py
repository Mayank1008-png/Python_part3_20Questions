#Def FUNCTION
#ans1
def num(a):
    if a%2==0:
        print('Number is Even')
    else:
        print('Number is Odd')
no=int(input('Enter any number to check EVEN/ODD='))
num(no)
#ans2
def numm(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * numm(n-1)
q=int(input('Enter any number to find factorial='))
print(f'factorial of {q} is {numm(q)}')
#ans3
def num(a):
    return a[::-1]
    
b=input('Enter any string=')
print(num(b))
#ans4
def check(strin):
    if (strin==strin[::1]):
        print(f'Yes {strin} is polindrome!')
    else:
        print('Not a Polindrome')
check('Madam')
#ans5
def maxi(a,b,c):
    if (a>=b and a>=c):
        print(f'Yes {a} is the maximum')
    elif (b>=a and b>=c):
        print(f'Yes {b} is the maximam number')
    else:
        print(f'Yes {c} is the maximum one')
maxi(7,8,9)
#ans6
def vowels(a1):
    cou=0
    for i in a1.lower():
        if i in 'a,e,i,o,u':
            cou+=1
    return cou
strq=input('Enter any string:-')
vow=vowels(strq)
print(f'Number of Vowels in {strq} is {vow}')
#ans7
def num(a):
    sum1=0
    while a>0:
        digit=a%10
        sum1+=digit
        a=a//10
    return sum1

p=int(input('Enter any number to find sum of their digits='))
v=num(p)
print(f'the sum of the digit of {p} is {v}')
#ans8
def fab(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
term=int(input('Enter any nymber to get Fibonacci series='))
for i in range(term):
    print(fab(i),end=' ')
#ans9  #GCD Greater COMMON Divisior
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a % b)
x=int(input('Enter first number to gcd='))
y=int(input('Enter sencond number to get gcd='))
print(f'the gcd of {x} and {y} is {gcd(x,y)}')
#Ans10
def num(n):
    if n<=1:
        return False
    for i in range(2,n//2 +1):
        if n%i==0:
            return False
    return True
nu=int(input('Enter a number='))
if num(nu):
    print(f'{nu} is the prime number')
else:
    print(f'{nu} is not a prime number')
#ans11
def sq(a):
    return a**2
def cube(a):
    return a**3
num=int(input('Enter any number to find square and cube='))
print(f'the square of {num} is {sq(num)}')
print(f'the cube of {num} is {cube(num)}')
#ans12
def year(a):
    if ((a%4==0 and a%100!=0) or a%400==0):
        print('Yes it is the leap year')
    else:
        print('No it is not a leap year')
year(1500)
#ans13
def lag(a):
    m=max(a)
    for i in a:
        if m==i:
            print(i)
lag(a=[1,2,3,9])
#ans14
def char(a):
    count=0
    for i in a:
        count+=1
    return count 
st=input('Enter any string to find character=')
vq=char(st)
print(f'the {st} has {vq} no of characters')
#ans15
def lst(a,b):
    summ=a+b
    return summ
lst1=[1,2,3,4]
lst2=[7,8,9]
print(lst(lst1,lst2))
#ans16 #list arrange without using sort()
def lst1(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                 a[j],a[j+1]=a[j+1],a[j]
    return a
my_list=[7,4,2,9,1]
sort=lst1(my_list)
print(my_list)
#ans17
def lst(a):
    dup=[]
    for i in a:
        if a.count(i)>1 and i not in dup:
            dup.append(i)
    return dup
my=[1,44,2,5,2,44]
print(f'duplicates are={lst(my)}')
#ans18
def dict1(a):
    sp=[]
    for x,y in a.items():
        print(f'{x}:{y}')
    return ','.join(sp)
dict2={'name':'mayank','age':19}
print(dict1(dict2))
#ans19
def si(p,r,t):
    return p*r*t/100
print(si(12000,2,12))
#ans20 #anagram
def st(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
s1=input('enter 1st string to check anagram=')
s2=input('enter 2nd string to check anagram=')
if st(s1,s2):
    print('Yes it is anagram')
else:
    print('NO its not a anagram')
#ans21
list1=[1,2,3,4,5]
def ls(l):
    pt=[]
    for i in l:
        if i%2==0:
            pt.append(i)
    return pt
print(ls(list1))
#ans22
def equivalent_number(n):
    return n

num = int(input("Enter a number: "))
print("Equivalent number is:", equivalent_number(num))
#ans 23
def fact(a):
    result=1
    for i in range(1,a+1):
        result*=i
    return result
print(fact(3))
#ans24
def fn(a):
    uni=list(set(a))
    uni.remove(max(a))
    return max(uni)   
print(fn([2,3,4,5,6]))
#ans25
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

my_list = [1, 2, 3, 4, 5]


# OOPS
#ans1
class person():
    name='Mayank'
    Grade='A'
student=person()
print(student.name,student.Grade)

#ans2
class rectangle:
    def __init__(self,lenght,breath):
        self.lenght=lenght
        self.breath=breath
    def area(self):
        return self.lenght*self.breath
    def parameter(self):
        return 2*(self.lenght+self.breath)
r=rectangle(12,13)
print('Area of rectangle is',r.area())
print('Paramenter of Rectangle is',r.parameter())
#ans3
class student:
    name='Mayank'
    grade='B'
stu1=student()
print(stu1.grade)
#ans4
class private_variable:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(f'name:{self.name}')
        print(f'age:{self.__age}')
p=private_variable('Mayank',12)
p.show()
#ans5
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" ₹{amount} deposited.")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print(" Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def show_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.__balance}")

account = BankAccount("Mayank", 1000)
account.show_info()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
print("Final Balance:", account.get_balance())
#ans6
class student:
    def __init__(self,name,emp_id,job_title):
        self.name=name
        self.emp_id=emp_id
        self.job_title=job_title
    def display(self):
        print(f'Name:{self.name}')
        print(f'Emp_ID:{self.emp_id}')
        print(f'Job_Title:{self.job_title}') 
t=student('Mayank',101,'Data Analyst')
t.display()   
#ans7
class animal: #PARENT
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f'{self.name} makes a sound')
class dog(animal): #CHILD
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def barks(self):
        print(f'{self.name} which is from {self.breed} breed sounds like : WOOF!')
d=dog('Bruno','Labara')
d.speak()
d.barks()
#ans 8
class puppy(dog):
    def __init__(self, name, breed,move):
        super().__init__(name, breed)
        self.move=move
    def w(self):
        print(f'{self.name} moves {self.move}')
pt=puppy('Tommy','German Shephard','Slowly')
pt.barks()
pt.w()
pt.speak()
#ans9
class school:
    school_name='Rao Man Singh'
    def __init__(self,stu_name,marks):
        self.stu_name=stu_name
        self.marks=marks
    #class-method
    def get(s):
        print('School Name =',s.school_name)
    #static-method
    def is_pass(marks):
        return marks>35
t=school('Mayank',88)
#call-class method
print(t.school_name)
t.get()
#call-statis method
print(f'DID {t.stu_name} pass?=',school.is_pass(t.marks))
#ans10
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
         return point(self.x + other.x,self.y+other.y)
    def display(self):
        print(f'{self.x}:{self.y}')
p1=point(4,5)
p2=point(3,2)
p3=p1+p2
p3.display()
#ans11
class anim:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f'{self.name} is the name of my pet')
    
class dog(anim):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        print(f'{self.name} is the name of my pet and breed is {self.breed}')
a=anim('Bruno')
d=dog('Tommy','Labera')
a.sound()
d.sound()        #override
#ans12
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal initialized: {self.name}")

    def sound(self):
        print(f"{self.name} makes a generic animal sound.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class __init__
        self.breed = breed
        print(f"Dog initialized: Breed = {self.breed}")

    def sound(self):
        super().sound()  # Optional: Call parent method
        print(f"{self.name} the {self.breed} barks: Woof!")

# Create object of Dog class
d = Dog("Tommy", "Labrador")
d.sound()
#ans13
class counter:
    count=0
    def __init__(self):
        counter.count+=1
        print(f'Object {counter.count} created')
    #class-method
    def get_count(cls):
        return cls.count
obj1=counter()
obj2=counter()
obj3=counter()
print('Total Objects created:',counter.get_count(obj1))
#ans14
class stu:
    def __init__(self,name,roll,job_title):
        self.name=name
        self.roll=roll
        self.job_title=job_title
    def __str__(self):
         print(f'Name={self.name},Roll_No={self.roll},Job_Title={self.job_title} ')
a1=stu('Mayank',100,'Data Analyst')
a1.__str__()
#ans15
class employee:
    def __init__(self,emp_name,emp_id,salary):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.salary=salary
    def get_salary(self):
        print(f'{self.emp_name} has salary around {self.salary}')
class manager(employee):
    def __init__(self, emp_name, emp_id, salary,manager_n):
        super().__init__(emp_name, emp_id, salary)
        self.manager_n=manager_n
    def info(self):
        print(f'{self.emp_name} has salary around {self.salary} and manager name is {self.manager_n}')
a=manager('Mayank',101,120000,'Akash Kumar')
a.info()

    