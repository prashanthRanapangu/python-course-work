bullets=10
while bullets>0:
    if bullets==5:
        print("Dead")
        break
    print(f"{bullets} are left ,you can shoot")
    bullets-=1
else:
    print("Gameover")


l=["smartphone","laptop","airpods","charger"]
for i in l:
    if i=="airpods":
        continue
    print(i.center(20,"-"))
else:
        print("Game over")


fact=0
n=int(input("enter a numnber:"))
for i in range (1,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f"{n} is prime number \nfactors count={fact}")
else:
    print(f"{n} is not a prime number \n factors count={fact}")

l=["apple","banana","milk"]
for i in range (len(l)):
    print(f"{i+1}.{l[i]}")
while True:
    l
