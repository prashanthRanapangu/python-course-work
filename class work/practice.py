'''num=int(input("Enter the number:"))
for i in range(num):
    print(i)

num=int(input("Enter a number"))
for i in range(num):
    if i % 2 == 0:
        print(i)

num=int(input("Enter the number: "))
total=0
for i in range(1, num+1):
    total+=i
print(total)

num= int(input("Enter the number: "))
for i in range(num):
    if i % 2 != 0:
        print(i) 
    #factorial numbers
num =int(input("Enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

#multiplication table
num=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{num} * {i}={num*i}") '''

#prime number
'''num=int(input("Enter a number:"))
if num<=2:
    print(num,"is not a prime ")
else:
    is_prime=True
    for i in range(2,int(num **0.5) + 1):
        if num %2 == 0:
            is_prime= False
        break
    if is_prime:
        print(num,"is prime")
    else:
        print(num,"not a prime")'''

#Finonacci series using for loop
'''num=int(input("enter"))
a, b=0,1
print("fibonacci:")
for i in range(num):
    print(a)
    a,b=b,a+b '''
#reverse numbers
num=int(input("Enter number:"))
while num>=1:
    print(num)
    num-= 1

'''def greet_user(name):
    print("Hello",name)
name=input("Enter your name:")
greet_user(name)
#square of a number
def square(num):
    print(num *num)
num=int(input("enter a number: "))
square(num)'''
#is_even
'''def is_even(n):
    if n%2==0:
        print("True")
    else:
        print("False")
n=int(input("Enter the number: "))
is_even(n)
def is_even(n):
    return n%2==0
n=int(input("Enter number: "))
print(is_even(n))
#count_vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
#reverse string
def reverse_true(s):
    return s[::-1]
s=input("enter a string: ")
print(reverse_true(s))
#factorial 
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact
n=int(input("Enter a number: "))
print(factorial(n))
#palindrome
def palindrome(s):
    return s[::-1]==s[:]
s=input("Enter a string: ")
print(palindrome(s))
#max 
def max_of_three(a,b,c):
    return max(a,b,c)
a,b,c=1,3,5
print(max_of_three(a,b,c))
 #count 
def count_words(s):
     return len(s.split())
     
s=input("Enter sentenses: ")
print(count_words(s))

#sumof digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n)) 
n=int(input("Enter a number: "))
print(sum_of_digits(n)) 
def fibonacci(n):
   a,b=0,1
   for _ in range(n):
       print(a,end='')
       a,b=b,a+b
n=int(input("Enter a number: "))
print(fibonacci(n)) '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    























