from csv import reader
from csv import DictReader

class Product:

    """*****for storing product*****"""

    def __init__(self , name , price):
      self.name = name
      self.price = price

class ProductStock:

    """*****for storing ProductStock*****"""

    def __init__(self , product , quantity):
      self.product = product
      self.quantity = quantity

class Shop:

    """*****for storing Shop details*****"""

    stock = []

    @classmethod
    def changeStock(cls , newStock):
        cls.stock.append(newStock)


class Customer:

    """*****for storing Customer Details*****"""

    shoppingList = []
    def __init__(self , name , budget):
        self.name = name
        self.budget = budget

    @classmethod
    def changeShoppingList(cls , item):
        cls.shoppingList.append(item)

def printProduct(p):

    """*****Function to print product name and price*****"""

    print("Product Name:", p.name ," \nProduct Price: " , p.price ,"\n")

def printCustomer(c):

    """*****Function to print whole details of customer i.e. name , budget , shopping List and its details*****"""

    for item in c.shoppingList:
        printProduct(item.product)
        print(c.name ,"orders", item.quantity ,"of above product\n")
        cost = item.quantity * item.product.price
        print("The cost to " , c.name ," will be " ,cost ,"\n")

def printCustomerTest(c):

    """*****Function to print whole details of customer i.e. name , budget , shopping List and its details*****"""

    print("Customer Name:" , c.name ,"\nCustomer Budget:" ,c.budget ,"\n")
    
    
def createAndStockShop():

    """*****for retrieving data from stock.csv FILE and use it accordingly.*****"""

    shop = Shop()
    
    fp = open("stock.csv","r") #*****FILE pointer which is opening the file stock.csv as in read mode*****
    first = fp.readline()
    split_line = first.split(",")
    cash = float(split_line[0])
    shop.cash = cash

    if(cash == None):
        exit()     #*****if file is empty ...*exit****

    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        name = split_line[0]
        
        if(split_line[1] != ''):
            price = float(split_line[1])    #*****converting to float*****
        else:
            price = 0.0

        if(split_line[2] != ''):
            quantity = int(split_line[2])   #*****converting to float*****
        else:
            quantity = 0
        
        #*****Now creating a new product and adding it to ProductStock as well as including it inm shop*****#

        product = Product(name , price)

        stockItem = ProductStock(product , quantity)

        shop.changeStock(stockItem)
        

    fp.close()       #closing file
    printShop(shop)
    return shop

def printShop(s):

    """******Function to print the details of shop i.e. cash , product stock and product details as well as quantity of each*****"""
    print("------------------------\n")
    print("CASH STATUS\n")
    print("Shop has " ,s.cash ," in cash\n")
    print("-------------\n")
    print("STOCK STATUS\n")

    for item in s.stock:
        printProduct(item.product)
        print("The Shop has ",item.quantity , " of the above\n")
        print(' ')

def checkStock(name , s):
    """******Function to check the details of shop stock i.e. product name *****"""
    
    for i in range(len(s.stock)):
        if(s.stock[i].product.name == name):
            return i
    return -1

def initiateShopping(customer , shop):
    """******Function to initiate purchase via CSV file *****"""
    index = 0
    totalCost = 0.0

    fp = open(customer,"r")

    if(fp == None):
        exit()     #*****if file is empty ...*exit****

    first = fp.readline()
    split_line = first.split(",")
    name = split_line[0]
    budget = float(split_line[1])

    c = Customer(name , budget)
    
    print("-------------\n")
    print("CUSTONMER ORDER- CSV FILE\n")
    print("Customer Name:" , c.name ,"\nCustomer Budget:" ,c.budget ,"\n")

    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        pName = split_line[0] 
        if(split_line[1] != ''):
            quantity = int(split_line[1])    #*****converting to float*****
        else:
            quantity = 0

        index = checkStock(pName,shop)
        
        if(index != -1):
            if(shop.stock[index].quantity >= quantity):
                cStock = ProductStock(shop.stock[index].product , quantity)
                c.changeShoppingList(cStock)
                shop.stock[index].quantity -= quantity
                cost = quantity * shop.stock[index].product.price
                totalCost += cost
                
            else:
                print("-------------\n")
                print("We have only",shop.stock[index].quantity , pName)
        else:
            print("-------------\n")
            print(pName," not available\n")
    
    
    printCustomer(c)
    shop.cash += totalCost
    print("-------------\n")
    print("The total cost to " , c.name ," will be " ,totalCost ,"\n")
    
    return shop

def initiateShoppingtest(customerTest, shop):
    """******Function to initiate purchase via CSV test file *****"""
    index = 0
    totalCost = 0.0

    fp = open(customerTest,"r")

    if(fp == None):
        exit()     #*****if file is empty ...*exit****

    first = fp.readline()
    split_line = first.split(",")
    name = split_line[0]
    budget = float(split_line[1])

    c = Customer(name , budget)
    
    print("-------------\n")
    print("CUSTONMER TEST ORDER - CSV TEST FILE\n")
    print("Customer Name:" , c.name ,"\nCustomer Budget:" ,c.budget ,"\n")

    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        pName = split_line[0] 
        if(split_line[1] != ''):
            quantity = int(split_line[1])    #*****converting to float*****
        else:
            quantity = 0

        index = checkStock(pName,shop)
        
        if(index != -1): #*****if it returns -1 from the checkstock function it enters the for loop conditions*****
            
            if(shop.stock[index].quantity >= quantity):
                cost = quantity * shop.stock[index].product.price
                
                if (cost > c.budget):
                    printProduct(shop.stock[index].product)
                    print(c.name ,"orders", quantity ,"of above product\n")
                    print(c.name, ", your budget is", c.budget, ", the total cost is ", cost, "you can not complete the order", "\n")
                else:
                    totalCost += cost
                    cStock = ProductStock(shop.stock[index].product , quantity)
                    c.changeShoppingList(cStock)
                    shop.stock[index].quantity -= quantity 
                    
                    
                    printProduct(shop.stock[index].product)
                    print(c.name ,"ORDERS", quantity ,"OF ABOVE PRODUCT\n")
            else:
                print("-------------\n")
                print("We have only",shop.stock[index].quantity , pName)
        else:
            print("-------------\n")
            print(pName," not available\n")
    
    shop.cash += totalCost
    
    print("-------------\n")
    print("The total cost to " , c.name ," will be " ,totalCost ,"\n")
    printShop(shop)

    return shop

def operatorOnline(shop):
    """******Function to initiate purchase in the live mode *****"""
    val = 0
    totalCost = 0

    name = input("Enter Your Name: ")
    budget = int(input("Enter your budget: "))
    c = Customer(name , budget)

    while(val < 256):
        pName = input("Enter name of Product: ")

        index = checkStock(pName , shop)
        if(index != -1):
            quantity = int(input("Enter quantity of Product: "))
            if(shop.stock[index].quantity >= quantity):
                cost = quantity * shop.stock[index].product.price
                
                
                if (cost > c.budget):
                    print(" ")
                    printProduct(shop.stock[index].product)
                    print(c.name ,"ORDERS", quantity ,"OF ABOVE PRODUCT\n")
                    print("-------------\n")
                    print(c.name, ", your budget is", c.budget, ", the total cost is ", totalCost, "you can not complete the order")
                else:
                    totalCost += cost
                    cStock = ProductStock(shop.stock[index].product , quantity)
                    c.changeShoppingList(cStock)
                    shop.stock[index].quantity -= quantity 
                    

            else:
                print("-------------\n")
                print("We have only",shop.stock[index].quantity , pName)
        else:
            print(pName," not available\n")
        val = int(input("If you want to add more product enter 0 else 1--->"))
        if(val == 1):
            break
    
    shop.cash += totalCost
    print("-------------\n")
    printCustomer(c)
    print("-------------\n")
    print("The total cost to " , c.name ," will be " ,totalCost ,"\n")
    printShop(shop)
    return shop

def menu(): 
    print("-------------\n")
    print("MENU")
    print("-------------\n")
    print("1 - order by csv file")
    print("2 - place your order in a live mode")
    

    while True:
               
        try:
            option = int(input("Choose your number (1 or 2): "))

            if (option == 1):
                shop = createAndStockShop()
                shop = initiateShopping("customer.csv", shop)
                printShop(shop)
                shop = initiateShoppingtest("customertest.csv", shop)
                
            elif (option == 2):
                shop = createAndStockShop()
                shop = operatorOnline(shop)
       
        except Exception as e:
            if e is ValueError or e is TypeError: 
                continue 
            
            else: 
                break
    return option 

#****Here  calling of function and real programming take place****#

if __name__ == "__main__":
  menu()






