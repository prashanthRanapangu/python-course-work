#1 Tuples
empty_tuple=()
single_tuple=(5,)
mytuple=(1,"apple",3.5)
implicit_tuple=1,2,3
#indexing 
mytuple1=(10,20,30,40)
print(mytuple1[2])        #30

#Negative indexing
print(mytuple1[-1])       #40
#slicing
print(mytuple1[0:])       #(10, 20, 30, 40)
print(mytuple1[1:5])     #(20, 30, 40)

#Operations on tuples 
#a.Concatination
con="Ranapangu"
cat="Prashanth"
print(con+cat)   #RanapanguPrashanth

#b.Repetation
print(con*3)       #Ranapangu Ranapangu Ranapangu
#c.membership Testing
print(20 in mytuple1)     #True
print("20" not in con )       #True
#Tuple Unpacking
grp=(1,2,3,4)
a,b,c,d=grp
print(a,b,c)       #1 2 3

#4.
print(grp.count(4))    #4
print(grp.index(2))    #1
print(len(grp))        #4
print(max(grp))        #4
print(min(grp))        #1
print(sum(grp))        #10

