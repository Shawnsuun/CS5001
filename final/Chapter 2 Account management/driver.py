from account_management import *
from admin_management import *

#initialize variables email and password as empty
email = ""
password = ""


def main():
	"""
	main function of the account management system

	"""  
	# menu text content
	menu = "Main menu\n"
	menu += "1. create account\n"
	menu += "2. login\n"
	menu += "3. change password\n"
	menu += "4. delete account\n"
	menu += "5. get all account information(admin password request)\n"
	menu += "6. quit\n"

	# boolean to decide if the program is running
	running = True

	# program loop
	while running:
		#globalize variables email and password
		global email
		global password

		# create an instance of class Account_management
		manager = Account_management()

		# create an instance of class Admin_management
		admin = Admin_management()

		# catch user input
		option = input(menu)

		# options which need to input email and password
		login_option = ['1', '2', '3', '4']

		# let user input email and password in list login_option
		if option in login_option:  
			email = input("please enter email: \n")
			password = input("please enter password: \n")

		#call respective class functions based on options
		if option == '1':
			manager.create_account(email, password)
		elif option == '2':
			manager.login(email, password)
		elif option == '3':
			new_password = input("please enter new password: \n")
			manager.change_password(email, password, new_password)
		elif option == '4':
			manager.delete_account(email, password)
		elif option == '5':
			# admin should login to print all emails and passwords
			admin_pass = input("please enter admin password: \n")
			if admin.admin_login(admin_pass):
				print(manager)
		elif option == '6':
			break
		else:
			print("invalid input")


#call main function
main()