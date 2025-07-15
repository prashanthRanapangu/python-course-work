for rows in range(5):
    for column in range(5):
        print(column,end='')
    print()

for rows in range(5):
    for column in range(5):
        print(rows,end='')
    print()

for row in range(5):
    for column in range(row+1):
        print("*",end='')
    print()

for row in range(5):
    for column in range(5-row):
        print("*",end='')
    print()

for row in range(5):
    for column in range(5-row-1):
        print(' ',end=' ')
    for clo1 in range(row+1):
        print("*",end=' ')

    print()

for row in range(5):
    for col in range(row):
        print(" ",end="")
    for column in range(5-row):
        print("*",end="")
    print()



'''n=int(input("enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print("*",end='')
        else:
            print(" ", end='')
    print()  

n=int(input("enter the size: "))
for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2:
            print("*",end='')
        else:
            print(" ", end='')
    print() '''

n=(int(input("enter numbers: ")))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=(int(input("enter numbers: ")))
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
