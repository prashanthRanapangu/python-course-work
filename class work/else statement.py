#example 1 
data={'prashanth@gmail.com':'123@',
      "vinay@gmail.com":"234@",
      "chotu@gmail.com":"456@"}

email,pwd=input("enter the email and pwd").split()
if data.get(email)==pwd:
    print("log in successful")
else:
    print("Invalid log in ")     #enter the email and pwdprashanth@gmail.com 123@ 
                                 #log in successful



