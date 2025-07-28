'''def display(name,pwd,email):
    print(name,email,pwd)

display(name='rushi',email='rushi@gmail.com',pwd='rushi@123')
#rushi rushi@gmail.com rushi@123

#positional Argument
def greet (name, age):
    print(f"Hello {name},you are {age} years old.")
greet ("Alice",25)      #Hello Alice,you are 25 years old.

#Keyword Arguments
greet(age=25,name="Alice")   #Hello Alice,you are 25 years old.

#Default Arguments
def greet (name,age=18):
    print(f"Hello {name}, you are {age} old")
greet("Bob")    #Hello Bob, you are 18 old

def bank(accno,pin):
    print(f"you bank accno is {accno}  and pin {pin}")
bank(1234,56787) #you bank accno is 1234  and pin 56787

def hospital(patient,disease):
    print(f"{patient} is suffering from {disease}")
hospital("raju","fever")   #raju is suffering from fever

#variable length Argument
def add (*numbers):
    return sum(numbers)
print(add(1,2,3,4,5))    #15

#keyword args 
def user_info(**details):
    fo key,value in details.items():
        print(f"{key}:{value}")

user_info(name="Alice",age=25,city="Newyork")'''

#functions based factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact= fact*i
    return fact


n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(f"{i}!={factorial(i)}")

#sum of numbers
    def sumofnumbers():
        s=0
        for i in range(1,n+1):
            s+=i
            return s
print(f"{n} ")
