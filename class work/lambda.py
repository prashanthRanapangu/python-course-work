n=3
sqn=lambda n: n*n
print(sqn(n))

l=[1,2,3,4]
squ=list(map(lambda i: i+10,l))
print(squ)

L=["sumith","saameer","tarak","dinesh","rushi"]
name=list(map(lambda i:i.title(),L))
print(name)

data={"mouse":True,'laptop':False,"soap":True,"phone":False,"charger":True}
d=list(filter(lambda i:data[i],data))
print(d)    #['mouse', 'soap', 'charger']


data={'dinesh':47,'mukesh':31,'gowtham':45}
d=dict(sorted(data.items(),keys=lambda i:1[1] reverse==True))
print(d)

