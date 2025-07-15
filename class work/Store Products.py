data={
    1:{"name":'milk','price':60},
    2:{'name':'Rice',"price":120},
    3:{'name':'salt','price':60},
    4:{'name':'bread','price':35},
    5:{'name':'avacado','price':70},
    6:{'name':'almonds','price':450},
    7:{'name':'cashew','price':550},
    8:{'name':'chia seeds','price':40},
    9:{'name':'flax seeds','price':50},
    10:{'name':'oats','price':160}
}
for i in range(1,11):
    print(f'{i}.{(data[i]["name"]).ljust(15," ")}:{data[i]["price"]}')
items=list(map(int,input("Enter item indexes:").split()))
print(items)
total =0
ids=set()
for i in items:
    if i not in ids:
        co=items.count(i)
        total+=(data[i]["price"]*co)
        print(f'{data[i]["name"]}-{co}*{data[i]["price"]}={data[i]["price"]*}')