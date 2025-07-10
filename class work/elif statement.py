#example 1
'''x=10
if x>25:
    print("A")
elif x>=20:
    print("B")
elif x<=8:
    print("C")
elif x<20:
    print("correct")
else:
    print("Wrong statement")   ##correct'''

#example 2
"""a=int(input("enter a :"))      #enter a :10
b=int(input("enter b :"))      #enter b :34
if a>b:
    print(f"{a} is greater than {b}")  
elif a==b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater than {a}") ##34 is greater than 10 """
#example 3
a=int(input("enter a  number:"))  #enter a  number:6
if a%2==0 and a%3==0:
    print("divisible by both 2 and 3") #divisible by both 2 and 3
elif a%2==0:
    print("divisible by only 2")
elif a%3==0:
    print("divisible by only 3")
else:
    print("not divisible by 2 0r 3 ")    
