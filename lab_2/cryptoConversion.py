from turtle import *

# Define a function to check if the currency amount user input is valid
def digit_input(msg_1, msg_2):
	invalid_input = True
	while invalid_input:
		currency_amount = input(msg_1) 
		currency_amount_trans = currency_amount.replace(".", "")
		if currency_amount_trans.isdigit():
			invalid_selection = False
			return currency_amount
		else:
			print (msg_2)

# Define a function to check if the user currency selection input is valid
def menu_selection(msg_1, msg_2):
	invalid_selection = True
	while invalid_selection:
		currency_index = input(msg_1) 
		currency_val = currency_vals.get(currency_index)
		if currency_val != None:
			invalid_selection = False
			return currency_index
		else:
			print (msg_2)


print ('Welcome to cryptoConversion!')

# Number of selections 1~5 and 5 currencies values(Equivalent to $100) are saved into dictionary "currency_vals"
usd_val = 100.0000
btc_val = 0.005354
eth_val = 0.077502
cny_val = 714.1244
currency_vals = {"1" : usd_val, "2" : btc_val, "3" : eth_val, "4" : cny_val}

# User input info based on previous "digit_input" and "menu_selection" functions
currency_amount = digit_input("\nPlease enter a currency amount :", "invalid input, please input int or float!")

currency_in = menu_selection("\nAmount entered was in what form?\nEnter:\n1.USD\n2.BitCoin\n3.Ethereum\n4.ChineseYuan\n", 
				"Please select an option from 1 ~ 4!")

currency_to = menu_selection("\nConvert the entered amount to what form?\nEnter:\n1.USD\n2.BitCoin\n3.Ethereum\n4.ChineseYuan\n", 
				"Please select an option from 1 ~ 4!")


# Calculate exchange rate and get final amount after convention
exchange_rate = currency_vals.get(currency_to)/currency_vals.get(currency_in)
final_amount = float(currency_amount) * exchange_rate


if currency_in == '1' or currency_to == '1':
	color('blue') 
	pendown()
	forward(100)
	left(90)
	forward(35)
	left(90)
	forward(100)
	right(90)
	forward(35)
	right(90)
	forward(100)
	penup()
	left(180)
	forward(50)
	right(90)
	forward(20)
	left(180)
	pendown()
	forward(110)
	penup()
	left(90)
	forward(70)
	pendown()
	if currency_in == '1':
		amount = currency_amount
	elif currency_to == '1':
		amount = final_amount
	color('purple') 
	write(f"USD {amount}",font = ("Arial", 10)) 
	penup()
	forward(200)

if currency_in == '2' or currency_to == '2':
	color('brown')
	pendown()
	left(90)
	forward(100)
	right(90)
	forward(25)
	circle(-25, 180)
	forward(25)
	left(180)
	forward(25)
	circle(-25, 180)
	forward(25)
	penup()
	left(180)
	forward(25)
	right(90)
	forward(10)
	left(180)
	pendown()
	forward(120)
	penup()
	left(180)
	forward(120)
	left(90)
	forward(50)
	if currency_in == '2':
		amount = currency_amount
	elif currency_to == '2':
		amount = final_amount
	color('black')
	write(f"BitCoin {amount}",font = ("Arial", 10)) 
	penup()
	forward(200)

if currency_in == '3' or currency_to == '3':
	color('red')
	pendown()
	left(60)
	forward(50)
	left(150)
	forward(27.5)
	right(60)
	forward(27.5)
	left(150)
	forward(50)
	left(150)
	penup()
	forward(40)
	pendown()
	right(60)
	forward(27.5)
	left(120)
	forward(27.5)
	left(60)
	forward(27.5)
	left(120)
	forward(27.5)
	right(180)
	forward(27.5)
	right(90)
	forward(45)
	right(120)
	forward(45)
	right(30)
	penup()
	forward(50)
	if currency_in == '3':
		amount = currency_amount
	elif currency_to == '3':
		amount = final_amount
	color('pink')
	write(f"Ethereum {amount}",font = ("Arial", 10)) 
	penup()
	left(90)
	forward(200)

if currency_in == '4' or currency_to == '4':
	color('green')
	pendown()
	left(90)
	forward(50)
	right(90)
	forward(35)
	right(180)
	forward(70)
	right(180)
	forward(35)
	left(90)
	forward(20)
	right(90)
	forward(35)
	right(180)
	forward(70)
	right(180)
	forward(35)
	left(45)
	forward(45)
	right(180)
	forward(45)
	right(90)
	forward(45)
	right(135)
	penup()
	forward(70)
	right(90)
	forward(100)
	left(90)
	if currency_in == '4':
		amount = currency_amount
	elif currency_to == '4':
		amount = final_amount
	color('red')
	write(f"ChineseYuan {amount}",font = ("Arial", 10)) 
	penup()
	forward(200)


mainloop()
