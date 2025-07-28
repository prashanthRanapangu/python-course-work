def feed(l):
    for i in l:
        yield i

l=['1..100','101...200','201...300','301..400']
load=feed(l)
print(next(load)) #1..100
print(next(load)) #101...200
'''prints only first elements from list when you calling through print statement.
no of callings =no of elements in the output'''


def simple():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=simple()
print(next(gen)) #start \n 1
print(next(gen)) # 2

def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count+=1
counter=count_up_to(5)
print(next(counter))
print(next(counter))

