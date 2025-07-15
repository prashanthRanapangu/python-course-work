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
#output 
#enter the mail: rigjaoweif
# Enter the pwd: ajrgo
#Invalid email or pwd.try again!!
#enter the mail: a;lrgj
#Enter the pwd: askjf
#Invalid email or pwd.try again!!
#enter the mail: asrgm xv
#Enter the pwd: ksnrgpiaer
#Invalid email or pwd.try again!!
#enter the mail: zsjd;
#Enter the pwd: asdknj
#Invalid email or pwd.try again!!
#enter the mail: a[wpszdvj
#Enter the pwd: a[w
#Invalid email or pwd.try again!!
#enter the mail: na'sdfv
#Enter the pwd: 'skndvpaw
#Invalid email or pwd.try again!!
#Max attempts are done.Try again after 5mins

#enter the mail: xyz@gmail.com
#Enter the pwd: xyz@2
#Log in succussfull