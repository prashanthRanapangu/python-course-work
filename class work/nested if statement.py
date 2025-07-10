#example 2
items=["coffe","icecream","samosa","idly"]
stock=[20,50,40,0]
data=input("enter the item:")
if data in items:
    ind=items.index(data)
    if stock[ind]>0:
        print("available")
    else:
        print("out of stock.please try again")
else:
    print("item not availabale ")  #enter the item:idly
                                   #out of stock.please try again