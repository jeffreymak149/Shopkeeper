# Shopkeeper
First python project (2019)

A python program to keep track of stocks sold via user input in terminal

To start the program, type python3 shopkeeper.py {starting price} {minimum price} {stock} in the terminal

Command:

sell {number of item you want to sell}
- sell items at current price after confirmation (yer or no) then display number of remaining stocks and how much money you gain

info
- Display current day, price, starting stock, remaining stock, total sales and both previous and current day's sales

next
- Display summary of current day and proceed to next day
- If current day's sales is fewer than previous day's sales by 10%, price of the stock will be reduced by 10 cents (0.1), 
  until the price is at the minimum price

end
- Quit program

Note: Since this is my first python program, all input are assumed to be in correct format/data type

