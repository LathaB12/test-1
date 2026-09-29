name=input("enter your name: ")

list= ""
#rice  Rs 10/kg
#sugar Rs 20/kg
#oil  Rs 30/litre
#salt Rs 5/kg
#cumin Rs 1/kg


price=0
pricelist=[]
totalprice=0
finaleprice=0
ilist=[]
qlist=[]
plist=[]

iteams={'rice':10, 'sugar':20, 'oil':30, 'salt':5, 'cumin':1}

while True:
    option=input("press 1 for list or 2 to exit:")
    if option=='2':
        print("thank you  for shopping")
        break
    elif option=='1':
        print(iteams)

        while True:
            if option == '1':
               item = input("choose your item:").lower()
            while True:
                quantity_input=input("enter quantity:")
                if quantity_input.isdigit():
                    quantity=int(quantity_input)
                    break
                else:
                    print("please enter a valid quantity:")
            if item in iteams:
                price= quantity* iteams[item]
                pricelist.append((item, quantity, iteams[item], price))

                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
            else:
                print("item not available")
        if totalprice>0:
            tax=(totalprice*18)/100
            finalamount=tax+totalprice
            
            print(25*"=","pythonlife supermarket",25*"=")
            print(28*"=","nellore")
            print("name:",name,30*"", "august 21 2023")
            print(75*"-")
            print("sno",10*" ","item",10*" ","quantity",10*" ","price")
            for i in range(len(pricelist)):
                print(i, 13*"", pricelist[i][0], 10*" ", pricelist[i][1], 10*" ", pricelist[i][2], 10*" ", pricelist[i][3])
            print(75*"-")
            print(50*" ", "totalamount:",'rs', totalprice)
            print("tax amount:",50*" ", 'rs', tax)
            print(75*"-")
            print(50*" ", "finalamount:",'rs', finalamount)
            print(75*"-")
            print(20*" ", "thank you for shopping with us")
            print(75*"-")


