#example 1
'''names=["vinay","chotu","muddu","vicky"]
for ch in names:
 print(f"ch={ch}")  #ch=vinay
                    #ch=chotu
                    #ch=muddu
                    #ch=vicky'''
#example 2
'''names={1:"vinay",2:"chotu",3:"muddu",4:"vicky"}
for i in names.keys():
 print(f"{i}-{names[i]}")   #1-vinay
                            #2-chotu
                            #3-muddu
                            #4-vicky'''
#example 3
'''names={1:"vinay",2:"chotu",3:"muddu",4:"vicky"}
for i in names.keys():
    print(f"{i}-{names[i].capitalize()}")      #1-Vinay
                                               #2-Chotu
                                               #3-Muddu
                                               #4-Vicky'''
#example 4
'''for i in range(1,21):
    print(f"5*{i}= {5*i}")'''
#Example 5
l=["vinay","chotu","muddu","vicky"]
for i in l:
    if i=="muddu":
        break
    print(i.center(20,"---"))
else:
    print("end of the names")