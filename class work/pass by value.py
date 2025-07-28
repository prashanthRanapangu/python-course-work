#int
def update(n):
    print("Before - inside of the function:",n)
    n=n+10
    print("After- inside of the function:",n)
n=10
update(n)
print("outside of the function:",n)

#string
def update(n):
    print("Before - inside of the function:",n)
    n=n+"programming"
    print("After- inside of the function:",n)
n="python"
update(n)
print("outside of the function:",n)

def update(n):
    print("Before - inside of the function:",n)
    n=n.append(4)
    print("After- inside of the function:",n)
n=[1,2,3]
update(n)
print("outside of the function:",n)

#dictionary
def update(n):
    print("Before - inside of the function:",n)
    n[6]=36
    print("After- inside of the function:",n)
n={1:1,2:4,3:9,4:16,5:25}
update(n)
print("outside of the function:",n)

#Boolean
def update(n):
    print("Before - inside of the function:",n)
    n=False
    print("After- inside of the function:",n)
n=True
update(n)
print("outside of the function:",n)

#
'''def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

n=int(input("Enter the value:"))
print(factorial(n))

###
def shoot(n):
    if n==1:
        return
    print("Before recursion",n)
    shoot(n-1)
    print("After recursion:",n)

n=int(input("Enter the value:"))
shoot(n)
##1
n=input("enter the num: ")
sum=0
for i in n:
    sum+=int(i)
print(sum)

#2 using recursion
n=int(input("Enter a number:"))
def sumofdigits(n):
    if n==0:
        return 0
    return n%10 + sumofdigits(n//10)
print(sumofdigits(n))'''
#fibonacci
n=int(input("Enter a number:"))
a,b= 0,1
print("fibonacci series:")
for i in range(n):
    print(a)
    a,b=b,a+b




