'''List in Python is a built-in Data structure that allows storing multiple values in a single variable.'''
#1.empty list
my_list = []  # Empty list 
my_list2 = list() 

#2.List with Elements.
number=[1,2,3,4,5]
fruits=["apple","banana","cherry"]
mixed=[10,"python",3.14,True]

#3.List with Nested List
nestedlist=[[1,2,3],["a","b","c"],[True,False]]
print(nestedlist[2])    #[True, False]
#4.List using List() Constructor
list_from_tuple=list((1,2,3))
string_to_list=list("Python") 
#Accessing elements in a list
#1.using indexing 
mylist3=["python","java","C++"]
print(number)     #[1, 2, 3, 4, 5] 
print(mylist3[0])     #python
print(mylist3[1])      #java
print(mylist3[2])      #c++
#2Using Slicing 
print(mylist3[0:])     #['python', 'java', 'C++']
print(mylist3[0:2])     #['python', 'java']
print(mylist3[-3:-2])    #['python']
print(mylist3[-1:])       #['C++']

#changing Elements
number=[1,2,3,4,5]
number[4]=6
#adding elements
print(number)         #[1, 2, 3, 4, 6]
number.append(7)
print(number)         #[1, 2, 3, 4, 6, 7]
number.insert(0,0)
print(number)          #[0, 1, 2, 3, 4, 6, 7]
number.extend([8,9,10])
print(number)            #[0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

#Removing Elements
number.remove(10)
print(number)      # [0, 1, 2, 3, 4, 6, 7, 8, 9]
number.pop(8)      
print(number)      # [0, 1, 2, 3, 4, 6, 7, 8]
del number[7]
print(number)      #[0, 1, 2, 3, 4, 6, 7]
number.clear()
print(number)      #[]

number=[0, 1, 2, 3, 4, 4, 7, 8, 9, 10]
print(number.count(4))    #2
number.reverse( )
print(number)    #[10, 9, 8, 7, 4, 4, 3, 2, 1, 0]
number.sort()
print(number) #[0, 1, 2, 3, 4, 4, 7, 8, 9, 10]
