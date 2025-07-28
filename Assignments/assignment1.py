#real-world example:Aha

#taking inputs from the user:
productID=int(input("enter product ID=")) 
ProductName=input("Enter your Product name:")
Price=float(input("enter price:"))
Catagory=list(input("enter your language:").split(','))
movie_genre=tuple(input("enter movie genres:").split(','))
Most_playtime=tuple(input("enter most playtime:").split(','))
Discount_Percentage=float(input("enter discount percentage:"))
Features=set(input("enter  features:").split(','))
Directors_name=eval(input("enter movie directors:"))
customercare_contact=int(input("enter customer care:"))
Location=input("enter location:")

#printing the inputs:
print(productID,ProductName,Price)
print(Discount_Percentage)

#types of Output Formatting:
#1️.Using Commas (Simple Print Method)
print(ProductName,Price,Discount_Percentage,movie_genre)
#output:Aha 1499.0 15.0 ('comedy', 'Horror', 'Romantic', 'Triller')

#2️.Using Modulo Operator (% Formatting)
print("price:%2f,productID:%d" %(Price,productID))
#output:price:1499.00,productID:1234

#3️.Using f-strings (Formatted String Literals) — Python 3.6+
print(f"features :{Features},location : {Location}")
#output:features :{'One device', 'multiple devices'},location : hyderabad

#4️.Using str.format() Method
print("productName:{}, productID:{}".format(ProductName,productID))
#output:productName:Aha, productID:1234


#outputs:
#enter product=1234
#Enter your Product name:Aha
#enter price:1499.00
#enter your Languages:Telugu,Hindi,English
#enter movie genres:comedy,Horror,Romantic,Triller
#enter most playtime:Saalar,KGF,Bahubali
#enter discount percentage:15.00
#enter features:One device,multiple devices
#enter movie directors:{"saalar":"Prashanth","bahubali":"Rajamouli"}
#enter customer care :987654321
#enter location:Hyderabad 
 