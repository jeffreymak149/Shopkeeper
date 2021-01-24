import sys
#python3 shopkeeper.py <starting price> <minimum price> <stock>
#Assume all arguments are positive number
#Assume stock as a whole number, minimum number <= starting price


#To start the program, type python3 shopkeeper.py {starting price} {minimum price} {stock} in the terminal

current_price = float(sys.argv[1])
minimum_price = float(sys.argv[2])
stock = int(sys.argv[3])
day = 0
stock_sold = 0
sales = 0
total_sales = 0
day_total_sales = 0
day_stock_sold = 0
previous_stock_sold = 0
previous_total_sales = 0
percentage_sales = 0
percentage_stock = 0
running = True

def sell(x):
    #I know this look messy, but I don't really know how to make it work without global everything.
    global stock
    global sales
    global stock_sold
    global total_sales
    global day_total_sales
    global day_stock_sold
    #local variable to global variable

    confirm = str(input("\n Are you sure you want to sell {} items? \n".format(x)))
    #confirmation, prevent typo
    var = int(x)
    if var < 0:
        print("Please enter a positive integer for stock")
    else:
        if confirm == "yes":
            if var > stock:
                print("There is not enough stock to sell({} items remaining \n)".format(stock))
            else:
                stock_sold = var
                sales = stock_sold * current_price
                total_sales += sales
                day_total_sales += sales
                day_stock_sold += stock_sold
                stock -= stock_sold
                print("\n You made ${:.2f} in selling {} items".format(sales, stock_sold))
                if stock == 0:
                    print("You have sold all your stock")
                    print("Your shop is now useless")
                    print("Perhaps a buying function need to be added")
                    #Maybe add a buying function
                else:
                    print("You have {} stock remaining".format(stock))
        elif confirm == "no":
            print("\n If you want to keep selling item, type sell (number of item you want to sell) \n")
        else:
            print("Please type yes or no \n")
            sell(x)

def next():
    #I know this look messy, but I don't really know how to make it work without global everything.
    global day
    global previous_stock_sold
    global previous_total_sales
    global day_stock_sold
    global day_total_sales
    global current_price

    day = day + 1

    if previous_stock_sold != 0 and previous_total_sales != 0:
        percentage_stock = float((day_stock_sold - previous_stock_sold) / previous_stock_sold)
    else:
        percentage_stock = 0

    print("\n Summary of day {}: {} stock were sold and {:.2f}$ have been made today.".format(day, day_stock_sold, day_total_sales))
    print("Percentage change in stock sold compared to yesterday: {:.2f}% \n".format(percentage_stock*100))

    previous_stock_sold = day_stock_sold
    previous_total_sales = day_total_sales
    day_stock_sold = 0
    day_total_sales = 0
    if percentage_stock < -0.1:
        current_price = current_price - 0.1
        print("Since stock sold today is strictly decreased from the previous day, current price is now 10 cents cheaper ({:.2f})".format(current_price))
        if current_price <= minimum_price:
            current_price = minimum_price
            print("Current price is now the minimum price you set ({:.2f})".format(current_price))
            print("It can't be lowered anymore \n")

def info():

    print("\n Today is day {}".format(day))
    print("Current price: {:.2f}".format(current_price))
    print("Starting stock: {}".format(sys.argv[3]))
    print("Total sales from day 1: {:.2f}".format(total_sales))
    print("Stock left: {}".format(stock))
    print("Total stock sold today: {}".format(day_stock_sold))
    print("Total sales made today: {:.2f}".format(day_total_sales))
    print("Total stock sold yesterday: {}".format(previous_stock_sold))
    print("Total sales made yesterday: {:.2f}\n ".format(previous_total_sales))

def left(s, amount):
    return s[:4]

#Basic information at the start
print("\n Starting price: {:.2f}, minimum price:{:.2f}, stock: {}.".format(current_price, minimum_price, stock))
print("\n Type sell (Number of item you want to sell)(No bracket) if you want to sell any items, or else type next.")
print("\n You can also type info to check the summary of the shop")
print("\n Type end to shutdown your shop, THERE WILL BE NO GOING BACK")

#The start of the main leep
temp = 0

while running:
    ans = input("")
    if ans == "info":
        info()
    if ans == "next":
        next()
    if left(str(ans), 4) == "sell":
        temp = (str.split(str(ans), " "))
        sell(int(temp[1]))
    if ans == "end":
        con = input("Are you SURE? ")
        if con == "yes":
            running = False
        else:
            print("Get back to the shop")
