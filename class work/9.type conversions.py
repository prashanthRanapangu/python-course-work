#Converting from int
int_a=25
print(float(int_a))    #25.0
print(str(int_a))       #'25'
print(bool(int_a))      #True,Non zero ints are True
'''print(list(int_a))      #int is not iterable 
print(set(int_a))       #int is not iterable 
print(tuple(int_a))     #int is not iterable 
print(dict(int_a))      #int is not iterable '''

#Converting from float
float_n=3.1
print(float(float_n))    #3.1  
print(str(float_n))       #'3.1'
print(bool(float_n))      #True,Non zero floats are True
'''print(list(int_a))      #float is not iterable 
print(set(int_a))       
print(tuple(int_a))     
print(dict(int_a))  '''

#Converting from String (str)
string_c='Prashanth'
#print(int(string_c))      #only numeric strings like "10","23"
#print(float(string_c))    #valid for float string   
print(str(string_c))       #prashanth
print(bool(string_c))      #True
print(list(string_c))      #['P', 'r', 'a', 's', 'h', 'a', 'n', 't', 'h']
print(set(string_c))       #{'P', 'h', 'n', 's', 't', 'r', 'a'}
print(tuple(string_c))     #('P', 'r', 'a', 's', 'h', 'a', 'n', 't', 'h')
#print(dict(string_c))     #needs key and value pair

#Converting from list
list_1=[1,2,3,4]
#print(int(list_1))
#print(float(list_1))
print(str(list_1))       #[1, 2, 3, 4]
print(bool(list_1))      #True
print(list(list_1))      #[1, 2, 3, 4]
print(set(list_1))       #{1, 2, 3, 4}
print(tuple(list_1))     #(1,2,3,4)
#print(dict(list_1))     # #needs key and value pair

#Converting from set
set_1={3,4,5,6}
#print(int(set_1))
#print(float(set_1))
print(str(set_1))       #{3, 4, 5, 6}
print(bool(set_1))      #True
print(list(set_1))      #[3, 4, 5, 6]
print(set(set_1))       #{3, 4, 5, 6}
print(tuple(set_1))     #(3, 4, 5, 6)
#print(dict(set_1))     # #needs key and value pair

#Conversion from tuple
tuple_1=(1,2,3,4)
#print(int(tuple_1))
#print(float(tuple_1))
print(str(tuple_1))       #(1, 2, 3, 4)
print(bool(tuple_1))      #True
print(list(tuple_1))      #[1, 2, 3, 4]
print(set(tuple_1))       #{1, 2, 3, 4}
print(tuple(tuple_1))     #(1, 2, 3, 4)
#print(dict(tuple_1))     # #needs key and value pair

#conversion from dict
dict_1={"roll":23,"name":"Prashanth","course":"Python"}
#print(int(dict_1))
#print(float(dict_1))
print(str(dict_1))       #{'roll': 23, 'name': 'Prashanth', 'course': 'Python'}
print(bool(dict_1))      #True
print(list(dict_1))      #['roll', 'name', 'course']
print(set(dict_1))       #{'roll', 'course', 'name'}
print(tuple(dict_1))     #('roll', 'name', 'course')
print(dict(dict_1))      #{'roll': 23, 'name': 'Prashanth', 'course': 'Python'}

#Converting from Bool
boolean=False
#print(int(boolean))
#print(float(boolean))
print(str(boolean))       #False
print(bool(boolean))      #False
#print(list(boolean))     
# #print(set(boolean))       
#print(tuple(boolean))     
#print(dict(boolean))    

