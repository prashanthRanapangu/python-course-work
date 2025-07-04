#Arithematic Operator 

a=10
b=20
print("addition of:",a+b)       #addition of: 30
print("subtraction of:",a-b)    #subtraction of: -10
print("multiplication of:",a*b) #multiplication of: 200
print("division of:",a/b)       #division of: 0.5
print("floatdiv of:",a//b)      #floatdiv of: 0
print("modulus of:",a%b)        #modulus of: 10
print("exponential of:",a^b)    #exponential of: 30

#comparison operator
c=20
d=40
print("Equal (==):",c==d)        #Equal (==): False
print("NotEqual (!=):",c!=d)     #NotEqual (!=): True
print("Greater than (>):",c>d)   #Greater than (>): False
print("less than (<):",c<d)      #less than (<): True
print("greaterEqual (>=):",c>=d) #greaterEqual (>=): False
print("LessEqual (<=):",c<=d)    #LessEqual (<=): True


#Assignment operattor 
x=30
x+=20                  #add and assign (+=) 50
print("add and assign (+=)",x)
x-=10                  #sub and assign (-=) 40
print("sub and assign (-=)",x)
x*=2                    #mul and assign (*=) 80
print("mul and assign (*=)",x)
x/=4                    #div and assign (/=) 20.0
print("div and assign (/=)",x)
x//10                   #floor div and assign (//=) 20.0
print("floor div and assign (//=)",x)
x%=10                    #mod and assign (/=) 0.0
print("mod and assign (/=)",x)
x**10                     #expo and assign (*=) 0.0
print("expo and assign (*=)",x)

#Logical Operator 
x=20
y=40
print(x>15 and y<50)
print(x>15 or y>50) 
print(x>30)

#Membership Operator 
fruits=["apple","mango","guava","kiwi"]
veggies=["carrot","radish","brinjal","cucumber"]
print(" musk "in fruits)
print("radish"in veggies)


names=('prashanth','sumanth','tarak','sanjay','charan')
print("in result:","rahul" in names) #in result: False
print("not in result:","suhas" not in names) #not in result: True

#Identity Operators 
l=[1,2,3,4]
b=[1,2,3,4]
print("l is b",l is b)     #l is b False
a=b #assigining b to a 
print("a is b:",a is b )   #a is b: True
print("id(l)",id(l))       #id(l) 2815952608776
print("id(b)",id(b))       #id(b) 2815952608072
print("id(a)",id(a))        #id(a) 2815952608072
print("a is not b:", a is not b)  #a is not b: False
print ("l is not b",l is not b)   #l is not b True

#Bitwise Operator 
#1- 001
#2= 010
#3= 011
#4= 100
#5= 101
#6= 110
#7=111

#example
x=2
y=5
print(x&y) #0
print(x|y) #7
print(x^y) #7
print(~x)  #-3
print(x<<1)#4
print(x>>1)#1
 
