email,pwd='xyz@gmail.com','xyz@2'
max_attempts=5
current_attempts=0
while current_attempts<=max_attempts:
    e=input("enter the mail: ")
    p=input("Enter the pwd: ")
    if e==email and p==pwd:
        print("Log in succussfull")
        break 
    else:
        print("Invalid email or pwd.try again!!")
    current_attempts+=1
else:
    print("Max attempts are done.Try again after 5mins ")
