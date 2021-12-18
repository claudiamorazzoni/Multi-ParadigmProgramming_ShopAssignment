#include <stdio.h>
#include <string.h>
#include <stdlib.h>


/*for storing product*/
struct Product
{
	char *name;
	double price;
	
};

/*for storing ProductStock*/
struct ProductStock
{
	struct Product product;
	int quantity;
};

/*for storing Shop details*/
struct Shop
{
	double cash;
	struct ProductStock stock[20];
	int index;
};

/*for storing Customer Details*/
struct Customer
{
	char *name;
	double budget;
	struct ProductStock shoppingList[10];
	int index;
};

/*Function to print product name and price*/
void printProduct(struct Product p)
{

	printf("\n");
	printf("Product name: %s \nProduct price: %.2f\n", p.name, p.price);
	printf("\n");
}

/*Function to print whole details of customer i.e. name , budget , shopping List and its details*/
void printCustomer(struct Customer c)
{
    double totalCost;
	printf("-------------\n");
	printf("Customer name: %s \nCustomer budget: %.2f\n", c.name, c.budget);
	

	for (int i = 0; i < c.index; i++)
	{
		printf("\n");
		printProduct(c.shoppingList[i].product);
		printf("%s orders %d of above product\n", c.name, c.shoppingList[i].quantity);
		printf("\n");
		double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
		totalCost += cost;
		printf("The cost to %s will be %.2f\n", c.name, cost);
	}
	printf("-------------\n");
	printf("Total cost to %s will be %.2f\n", c.name ,totalCost);
	printf("-------------\n");
}


/*for retrieving data from stock.csv FILE and use it accordingly.*/ 
struct Shop createAndStockShop()
{
	FILE *fp;						       //FILE pointer
	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	fp = fopen("stock.csv", "r");	   //opening the file stock.csv as in read mode
	read = getline(&line, &len, fp);
	char *c = strtok(line, ",");
	double cash = atof(c);
		
	if (fp == NULL)
		exit(EXIT_FAILURE);				   //if file is empty ...*exit*

	struct Shop shop = { cash };

	while ((read = getline(&line, &len, fp)) != -1)
	{
		char *n = strtok(line, ",");		//taking first char pointer separated by "," 
		char *p = strtok(NULL, ",");		//taking next char pointer
		char *q = strtok(NULL, ",");
		int quantity = atoi(q); 			// converting q(String) to int
		double price = atof(p);				// converting p(String) to double
		char *name = malloc(sizeof(char) * 50);     //allocating memory to variable name
		strcpy(name, n);
		/*Now creating a new product and adding it to ProductStock as well as including it inm shop*/
		struct Product product = {name, price};
		struct ProductStock stockItem = {product, quantity};
		shop.stock[shop.index++] = stockItem;
	}

	fclose(fp);
	
	return shop;
}

/*Function to print the details of shop i.e. cash , product stock and product details as well as quantity of each*/
void printShop(struct Shop s)
{
	printf("-------------\n");
	printf("CASH STATUS\n");
	printf("Shop has %.2f in cash\n", s.cash);
	printf("\n");
	printf("-------------\n");
    printf("STOCK STATUS\n");

	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("\n");
		printf("The shop has %d of the above\n", s.stock[i].quantity);
	}
}

/*Function to check the details of shop stock i.e. product name */
int checkStock(char * name , struct Shop s)
{
    for (int i = 0; i < s.index; i++)
    {
        if(strcmp(s.stock[i].product.name , name) == 0 )
        {
            return i;
        }
    }
    return -1;
}

/*Function to initiate purchase via CSV file */
struct Shop initiateShopping(struct Shop shop)
{
    
    int index;
    double totalCost = 0;
    
    FILE *fp;
    char *line = NULL;
	size_t len = 0;
	ssize_t read;
	
	fp = fopen("customer.csv","r");
	if(fp == NULL)
	    exit(EXIT_FAILURE);
	    
	read = getline(&line, &len, fp);
	
	char *n = strtok(line, ",");
	char *p = strtok(NULL, ",");
	double budget = atof(p);
	char *name = malloc(sizeof(char) * 50);
	strcpy(name, n);
	
	struct Customer c = { name, budget };

	
		printf("-------------\n");
		printf("CUSTONMER ORDER- CSV FILE\n");

    	while ((read = getline(&line, &len, fp)) != -1)
	{
		
		char *s = strtok(line, ",");		//taking first char pointer separated by "," 
		char *q = strtok(NULL, ",");		//taking next char pointer
		int quantity = atoi(q); 			// converting q(String) to int
		char *stockName = malloc(sizeof(char) * 50);     //allocating memory to variable name
		strcpy(stockName, n);
		
		index = checkStock(stockName,shop);

		
		if(index != -1)
		{
			
		    if(shop.stock[index].quantity >= quantity)
		    {
		        struct ProductStock cStock = {shop.stock[index].product , quantity };
		        c.shoppingList[c.index++] = cStock;
		        shop.stock[index].quantity -= quantity;
		        double cost = quantity * shop.stock[index].product.price;
		        totalCost += cost;
		    }else
		    {
		        printf("-------------\n");
		        printf("We have only %d  %s\n", shop.stock[index].quantity , stockName);   
		    }
		}else
		{
		    printf("-------------\n");
		    printf("%s not available\n",stockName);
		}
	}
	printCustomer(c);
	
	shop.cash += totalCost;
	
	return shop;
}

/*Function to initiate purchase via CSV file */
struct Shop initiateShoppingTest(struct Shop shop)
{
    
    int index;
    double totalCost = 0;
    
    FILE *fp;
    char *line = NULL;
	size_t len = 0;
	ssize_t read;
	
	fp = fopen("customertest.csv","r");
	if(fp == NULL)
	    exit(EXIT_FAILURE);
	    
	read = getline(&line, &len, fp);
	
	char *n = strtok(line, ",");
	char *p = strtok(NULL, ",");
	double budget = atof(p);
	char *name = malloc(sizeof(char) * 50);
	strcpy(name, n);
	
	struct Customer c = { name, budget };

	
		printf("-------------\n");
		printf("CUSTONMER TEST ORDER - CSV TEST FILE\n");
		printf("\n");
		printf("Customer name: %s \nCustomer budget: %.2f\n", c.name, c.budget);
		printf("\n");

    	while ((read = getline(&line, &len, fp)) != -1)
	{
		
		char *s = strtok(line, ",");		//taking first char pointer separated by "," 
		char *q = strtok(NULL, ",");		//taking next char pointer
		int quantity = atoi(q); 			// converting q(String) to int
		char *stockName = malloc(sizeof(char) * 50);     //allocating memory to variable name
		strcpy(stockName, n);
		
		index = checkStock(stockName,shop);

		
		if(index != -1)
		{
		    if(shop.stock[index].quantity >= quantity)
		    {	
				double cost = quantity * shop.stock[index].product.price;
				

				if(cost > budget)
				{
					printf("Product Name: %s\n", shop.stock[index].product);
					printf("Product Price:%.2f\n", shop.stock[index].product.price);
					printf("%s orders %d of above product\n", name, quantity);
					printf("%s your budget is %lf the total cost is %f you can not complete the order\n", name, budget, cost);
					printf("\n");

				}else
				{

					totalCost += cost;
					struct ProductStock cStock = {shop.stock[index].product , quantity };
		        	c.shoppingList[c.index++] = cStock;
		        	shop.stock[index].quantity -= quantity;

				}
			
		        
		    }else
		    {
		        printf("-------------\n");
		        printf("We have only %d  %s\n", shop.stock[index].quantity , stockName);   
		    }
		}else
		{
		    printf("-------------\n");
		    printf("%s not available\n",stockName);
		}
	}
	
	printCustomer(c);
	shop.cash += totalCost;
	
	return shop;
}

/*Function to initiate purchase in the live mode */
struct Shop operatorOnline(struct Shop shop)
{
	int val = 0, quantity;
	double budget;
    char temp;
    char name[20] , pName[20];
	double cost;
    double totalCost;
    
	printf("Enter your Name:\n");
    scanf("\n%20[^\n]s",name);
    scanf("%c",&temp);
    
	printf("Enter your budget:\n");
    scanf("%lf",&budget);
    
	struct Customer c = {name, budget};
    
    
    while(val == 0)
    {
		printf("Enter name of Product:\n");
        scanf("\n%20[^\n]s",pName);
        
        int index = checkStock(pName , shop);

        if(index != -1)
        {
            printf("Enter quantity of Product\n");
            scanf("%d",&quantity);

            if(shop.stock[index].quantity >= quantity)
		    {	
				double cost = quantity * shop.stock[index].product.price;

				if(cost > budget)
				{
					printf("Product Name: %s\n", shop.stock[index].product);
					printf("Product Price:%.2f\n", shop.stock[index].product.price);
					printf("%s orders %d of above product\n", name, quantity);
					printf("%s your budget is %lf the total cost is %f you can not complete the order\n", name, budget, cost);

				}else
				{

					totalCost += cost;
					struct ProductStock cStock = {shop.stock[index].product , quantity };
		        	c.shoppingList[c.index++] = cStock;
		        	shop.stock[index].quantity -= quantity;

					printf("Product Name: %s\n", shop.stock[index].product);
					printf("Product Price:%.2f\n", shop.stock[index].product.price);
					printf("%s orders %d of above product\n", name, quantity);
					printf("The cost to %s will be %.2f\n", name, cost);
				}
			
		        
		    }else
		    {
		        printf("-------------\n");
		        printf("We have only %d  %s\n", shop.stock[index].quantity , pName);   
		    }
		    
        }else
        {
            printf("%s not available\n",pName);
        }
        
        printf("If you want to add more product enter 0 else 1\n");
        scanf("%d",&val);
        scanf("%c",&temp);
    }

	shop.cash += totalCost;

	
	
	printf("-------------\n");
    printf("%s pay the total Amount of %.2f \n",name , totalCost);
    
    return shop;
}

/*main function which serves as the starting point for program execution*/
int main()
{
	
	printf("-------------\n");
	printf("MENU\n");
	printf("-------------\n");
	printf("\n1 - order by csv file");
	printf("\n2 - place your order in a live mode");
	int choice = -1;

	while (choice != 0){
		fflush(stdin);
		printf("\nChoose your number (1 or 2): ");
		scanf("%d", &choice);

		if (choice == 1){
			struct Shop shop = createAndStockShop();
			printShop(shop);
			shop = initiateShopping(shop);
			printShop(shop);
			shop = initiateShoppingTest(shop);
			printShop(shop);
		} else if (choice == 2){
			struct Shop shop = createAndStockShop();
			printShop(shop);
			operatorOnline(shop);
		}
	}
	printf("Press 1 or 2");

	return choice;
}