import itertools

#*****Global variables*****
stock = []
stockCash = []
productName = []
productPrice = []
productQuantity = []
customerName = []
customerBudget = []
customerProduct = []
customerQuantity = []
shoppingList = []
operatorOnlineList = []
customerTestName = []
customerTestBudget = []

def cash ():
    """*****for retrieving cash data from stock.csv FILE and use it accordingly.*****"""
    fp = open("stock.csv","r") #*****FILE pointer which is opening the file stock.csv as in read mode*****
    first = fp.readline()
    split_line = first.split(",")
    cash = float(split_line[0])
    stockCash.append(cash)
    
    return stockCash

def createAndStockShop():
    """*****for retrieving data from stock.csv FILE and use it accordingly.*****"""
    shop = stock
    fp = open("stock.csv","r") #*****FILE pointer which is opening the file stock.csv as in read mode*****
    first = fp.readline()
    split_line = first.split(",")
    cash = float(split_line[0])
    stockCash.append(cash)
       

    for line in fp:
        
        split_line = line.split(",")   #*****spliting the line by ","*****
        name = split_line[0]
        productName.append(name)
        

        if(split_line[1] != ''):
                price = float(split_line[1])    #*****converting to float*****
                productPrice.append(price) 
        else:
            price = 0.0

        if(split_line[2] != ''):
            quantity = int(split_line[2])   #*****converting to float*****
            productQuantity.append(quantity)
        else:
            quantity = 0
    
    fp.close() 
    return printShop()

def printShop():

    """******Function to print the details of shop i.e. cash , product stock and product details as well as quantity of each*****"""
    print("-------------\n")
    print("CASH STATUS\n")
    print("Shop has " ,stockCash[0] ," in cash\n")
    print("-------------\n")
    print("STOCK STATUS\n")
    
    
    for itemName, itemPrice, itemQuantity in itertools.zip_longest (productName, productPrice, productQuantity, fillvalue=0):
        
        print("Product Name: ", itemName, " \n")
        print("Product Price: ",itemPrice , " \n")
        print("The Shop has ",itemQuantity , " of the above\n")
        print("")

def printCustomer(totalcost):
    """*****Function to print whole details of customer i.e. name , budget , shopping List and its details*****"""

    print("-------------\n")
    print("The total cost to " , customerName[0] ," will be " ,totalcost ,"\n")
        

def checkStock(name):
    """******Function to check the details of shop stock i.e. product name *****"""
    for i in range(len(productName)):
        if(productName[i] == name):
            return i
    return -1

def changeShoppingList(item):
        shoppingList.append(item)

def initiateShopping(customer):
    """******Function to initiate purchase via CSV file *****"""
    index = 0
    totalCost = 0.0
    
    fp = open(customer,"r")

    if(fp == None):
        exit()     #*****if file is empty ...*exit****

    first = fp.readline()
    split_line = first.split(",")
    name = split_line[0]
    customerName.append(name)
    budget = float(split_line[1])
    customerBudget.append(budget)
    
    print("-------------\n")
    print("CUSTOMER ORDER - CSV FILE\n")
    print("Customer Name:" , name ,"\nCustomer Budget:" ,budget ,"\n")


    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        pName = split_line[0]
        customerProduct.append(pName)
        if(split_line[1] != ''):
            quantity = int(split_line[1])    #*****converting to float*****
            
            customerQuantity.append(quantity)
        else:
            quantity = 0
        
        index = checkStock(pName)
        

        if(index != -1):
            if(productQuantity[index] >= quantity):
                
                cStock = (productName[index], productQuantity[index], productPrice[index])
                
                changeShoppingList(cStock)
                productQuantity[index] -= quantity
                cost = quantity * productPrice[index]
                totalCost += cost
                
                print("Product Name: ", productName[index])
                print("Product Price: ", productPrice[index])
                print(customerName[0] ,"ORDERS", quantity ,"OF ABOVE PRODUCT\n")
                print("The cost to " , customerName[0] ," will be " ,cost ,"\n")
                
            else:
                print("-------------\n")
                print("We have only",productQuantity[index] , pName)
        else:
            print("-------------\n")
            print(pName," not available\n")
    
    stockCash[0] += totalCost
    printCustomer(totalCost)
    
    return printShop()

def initiateShoppingtest(customerTest):
    """******Function to initiate purchase via CSV test file *****"""
    index = 0
    totalCost = 0.0
    
    fp = open(customerTest,"r")

    if(fp == None):
        exit()     #*****if file is empty ...*exit****

    first = fp.readline()
    split_line = first.split(",")
    name = split_line[0]
    customerTestName.append(name)
    budget = float(split_line[1])
    customerTestBudget.append(budget)
    
    print("-------------\n")
    print("CUSTONMER TEST ORDER - CSV TEST FILE\n")
    print("Customer Name:" , name ,"\nCustomer Budget:" ,budget ,"\n")

    for line in fp:
        split_line = line.split(",")   #*****spliting the line by ","*****
        pName = split_line[0]
        customerProduct.append(pName)
        if(split_line[1] != ''):
            quantity = int(split_line[1])    #*****converting to float*****
            customerQuantity.append(quantity)
        else:
            quantity = 0
        
        index = checkStock(pName)
        

        if(index != -1):
            if(productQuantity[index] >= quantity):
                cost = quantity * productPrice[index]
                totalCost += cost

                if (cost > budget):
                    print("Product Name: ", productName[index])
                    print("Product Price: ", productPrice[index])
                    print(customerTestName[0] ,"ORDERS", quantity ,"OF ABOVE PRODUCT\n")
                    print(customerTestName[0], ", your budget is", budget, ", the total cost is ", cost, "you can not complete the order", "\n")

                else:
                    cStock = (productName[index], productQuantity[index])
                    changeShoppingList(cStock)
                    productQuantity[index] -= quantity
                    stockCash[0] += cost
                    print("Product Name: ", productName[index])
                    print("Product Price: ", productPrice[index])
                    print(customerTestName[0] ,"ORDERS", quantity ,"OF ABOVE PRODUCT\n")
                    print("The cost to " , customerTestName[0] ," will be " ,cost ,"\n")
                    
            else:
                print("-------------\n")
                print("We have only",productQuantity[index] , pName)
        else:
            print("-------------\n")
            print(pName," not available\n")
    
    
    
    return printShop()

def operatorOnline():
    """******Function to initiate purchase in the live mode *****"""
    val = 0
    totalCost = 0

    name = input("Enter Your Name: ")
    customerTestName.append(name)
    budget = int(input("Enter your budget: "))
    customerTestBudget.append(budget)

    while(val < 256):
        pName = input("Enter name of Product: ")

        index = checkStock(pName)
        if(index != -1):
            quantity = int(input("Enter quantity of Product: "))
            if(productQuantity[index] >= quantity):
                cost = quantity * productPrice[index]
                

                if (cost > budget):
                    
                    print(" ")
                    print("Product Name:", productName[index])
                    print("Product Price: ", productPrice[index])
                    print(customerTestName[0] ,"ordes", quantity ,"of above product\n")
                    print(customerTestName[0], ", your budget is", budget, ", the total cost is ", cost, "you can not complete the order", "\n")
                else:
                    totalCost += cost
                    cStock = (productName[index], productQuantity[index])
                    changeShoppingList(cStock)
                    productQuantity[index] -= quantity
                    
                    print("Product Name:", productName[index])
                    print("Product Price: ", productPrice[index])
                    print(customerTestName[0] ,"ordes", quantity ,"OF ABOVE PRODUCT\n")
                    print("The cost to " , customerTestName[0] ," will be " ,cost ,"\n")
            
            else:
                print("-------------\n")
                print("We have only",productQuantity[index] , pName)
        else:
            print("-------------\n")
            print(pName," not available\n")
        val = int(input("If you want to add more product enter 0 else 1--->"))
        if(val == 1):
            break

    stockCash[0] += totalCost
    print("-------------\n")
    print("The total cost to " , name ," will be", totalCost ,"\n")
    return printShop()

def menu(): #function that display the menu
    print("-------------\n")
    print("MENU")
    print("-------------\n")
    print("1 - order by csv file")
    print("2 - place your order in a live mode")
    
    while True:
               
        try:
            option = int(input("Choose your number (1 or 2): "))

            if (option == 1):
                createAndStockShop()
                initiateShopping('customer.csv')
                initiateShoppingtest('customertest.csv')
                
            elif (option == 2):
                createAndStockShop()
                operatorOnline()
       
        except Exception as e:

            if e is ValueError or e is TypeError: #if user entered strings(not integer)
                continue #keep asking for input
            
            else: #if an integer is provided, then stop asking for input
                break
 
    return option #return the input


#****Here  calling of function and real programming take place****#

if __name__ == "__main__":
  menu()

