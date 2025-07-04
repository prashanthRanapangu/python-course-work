1.#case conversion methods
 #upper() and lower ()
text="ranapangu"
print(text.upper())  #RANAPANGU
print(text.lower())  #ranapangu
print(text.capitalize()) #Ranapangu
cl="ranapangu prashanth"
print(cl.title())  #Ranapangu Prashanth
cl1="PYthon"
print(cl1.swapcase()) #pyTHON

2.#Alignment & Formatting Methods
text="Python"
c1="call"
print(text.center(9, "*"))  #**Python*
print(c1.ljust(6, "-"))     #call--
print(c1.rjust(6, "-"))     #--call
print(c1.zfill(5))         #0call , Zfill=pads the strings with zeros on the left
###"Name:{},Age:{}".format("Tom",25)
##"{Name} is {age}",format_map({'name':'Tom','age':25})
3 #Search &find Methods
text1="Hello"
print(text1.find("o")) #4,Returns the index of first occurrence, -1 if not found. 
print(text1.rfind("l")) #3,returns last occurance
print(text1.index("e")) #1,Like find(), but raises an error if not found. 
print(text1.rindex("l")) #3 
print(text1.count("l"))  #2
#string Testing Method (Boolean Results)
print(text1.startswith("He")) #true
print(text1.endswith("llo"))  #True
print(text1.isalpha())    #True
print(text1.isdigit())    #false
text2="hello123"
print(text2.isalnum())   #True
print(text1.islower())   #False
print("HELLO".isupper())  #True
print(" ".isspace())      #True
print("Hello World".istitle()) #True
print("123".isdecimal())   #True
print(" 1/5".isnumeric())  #false
print("variable1".isidentifier()) #True
print("1/2".isdigit())       #false

5.#Replace & Modify methods
print("apple".replace("p","b"))  #abble
print("junior NTR".translate(str.maketrans("junior","Senior")))   #Senior NTR
print(str.maketrans("ae","12"))   #{97: 49, 101: 50} Creates a translation table for translate().   

#Splitting & Joining Methods
#split() 
sentence= "apple,banana,grape"
fruits=sentence.split(",")
print(fruits)      #['apple', 'banana', 'grape']
print(sentence.rsplit(",",1))  #['apple,banana', 'grape']
print(sentence.splitlines())  #['apple,banana,grape']  ,splitlines divides based on the lines ,if words are from different lines it splits 
#join()
joined="-".join(fruits)      #apple-banana-grape 
print(joined)
print("Ranapangu-Prashanth".partition("-"))  #('Ranapangu', '-', 'Prashanth')
print("Ranapangu-Prashanth".rpartition("-"))  #('Ranapangu', '-', 'Prashanth')
7.#Whitiespace & Trimming Methods
#strip()
rana =" python "
print(rana.strip())            #python
print("---hello".lstrip("-"))   #hello
print("hello---".rstrip("-"))    #hello
8.#encoding and decoding
text="prashanth"
print(text.encode())          #b'prashanth'
print(b'prashanth'.decode())   #prashanth
