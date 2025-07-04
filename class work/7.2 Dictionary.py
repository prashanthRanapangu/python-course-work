#syntax of Dictionary
#Dictionary_Name={key1:value1, key2:value2, key3:value3}
#Accesing values 

Student={"Name":"Alice","Age":23,"course":"Computer Science"}
print(Student)   #{'Name': 'Alice', 'Age': 23, 'course': 'Computer Science'}
print(Student["Name"]) #Alice
print(Student["Age"])  #23
print(Student["course"])  #Computer Science
print(Student.get("branch","not available")) #not available
#Adding and Updating Items

Student["Age"]=22
print(Student)
Student["city"]="NewYork"
print(Student)     #{'Name': 'Alice', 'Age': 22, 'course': 'Computer Science', 'city': 'NewYork'}

#Removing items from a Dictionary
Age=Student.pop("Age")
print(Student)     #{'Name': 'Alice', 'course': 'Computer Science', 'city': 'NewYork'} 
print(Age)         #22
del Student["course"]
print(Student)     #{'Name': 'Alice', 'city': 'NewYork'}
Student.clear()
print(Student)    #{}

# Dictionary Methods for Accessing Data 
Student={"Name":"Alice","Age":23,"course":"Computer Science"}
print(Student.keys()) #dict_keys(['Name', 'Age', 'course'])
print(Student.values()) #dict_values(['Alice', 23, 'Computer Science'])
print(Student.items()) #dict_items([('Name', 'Alice'), ('Age', 23), ('course', 'Computer Science')])

#Built-in Functions for Directions
print(len(Student))   #3
print(max(Student))   #course
print(min(Student))   #age
print(sorted(Student)) #'age','Name','Course'

#Nested dictionary
Students={"Alice":{"age":21,"course":"CS"},
          "Bob":{"age":22,"course":"Math"}}
print(Students["Alice"]["course"])   #CS

