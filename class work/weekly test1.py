#1
'''date,month,year=input().split('-')
print(f"{year}/{month}/{date}")'''
#2
n=int(input("enter a number:"))
if n%2==0:
    print("Even Winner")
else:
    print("odd winner") 
 #3
flt=list(map(float,input("enter number:").split()))
print(sum(flt))
print(max(flt)) 


'''n=input().lower()
print(n.translate(str.maketrans('aeiou','*****')))'''

'''credentials=("admin","python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
    print("log in succesful")
else:
    print("Acces denied")

n=int(input())
data={}
max_value=0
res=''
for i in range(n):
    name,mark=input().split()
    mark=int(mark)
    if marks>max_value:
        res=name
    data[name]=mark
print(data)
print(name)'''

#8
'''n=input().split()
for i in range(len(n)):
    n[i]=n[i][ :: -1]
print(''.join(n))'''

#9
'''s=input()
s=s.replace('0','')
print(s.split())'''

#10
'''n=input()
res={}
for i in n:
    if i not in res:
        res[i]=n.count(i)
print(res)'''
