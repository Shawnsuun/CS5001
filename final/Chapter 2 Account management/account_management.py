class Account_management:


	def __init__(self, emails = set(), passwords = {}):
		"""
		constructor of class Account_management

		key attributes:

		emails -- a set saving all the user emails, initialized as empty

		passwords -- a dictionary saving user email and password mapping, initialized as empty

		"""        
		self.emails = emails
		self.passwords = passwords


	def __str__(self):
		"""
		class objects as a string of all email and password mapping

		"""
		msg = ""
		# traverse the key, value of the password dictionary add to msg
		for email, password in self.passwords.items():
			msg += "\n"
			msg += email + " : " + password
		return msg


	def valid_email_format(self, email):
		"""
		check the email string, return true if valid
		
		key attributes:

		email -- a string of email

		"""
		# a valid email string should end with '@northeastern.edu'
		if email.endswith('@northeastern.edu'):
			return True
		return False


	def valid_password_len(self, password):
		"""
		check the password string, return true if valid
		
		key attributes:

		password -- a string of password

		"""
		# a valid password string should no less than 8 characters
		if len(password) < 8:
			return False
		return True

		
	def create_account(self, email, password):
		"""
		let the user input email and password to create an account

		key attributes:

		email -- a string of email

		password -- a string of password	

		"""
		# use try-except construct to catch errors
		try:
			# raise an error if email is not valid
			if not self.valid_email_format(email):
				raise ValueError("Email should end with '@northeastern.edu'") 
			
			# raise an error if password is not valid
			if not self.valid_password_len(password):
				raise ValueError("Password should be at least 8 characters") 
			
			# raise an error if password is already registered
			if email in self.emails:
				raise ValueError("The email is already used") 				
			
			# add email to set emails
			self.emails.add(email)

			# add email, password mapping to dictionary passwords
			self.passwords[email] = password
			print(f"{email} account successfully created!")

		# except error and give error message	
		except ValueError as ex:
			print(ex)	


	def login(self, email, password):
		"""
		let the user input email and password to login, return True if successfully login

		key attributes:

		email -- a string of email

		password -- a string of password	

		"""
		# use try-except construct to catch errors
		try:
			# raise an error if email is not registered
			if email not in self.emails:
				raise ValueError("Email not registered!") 

			# raise an error if password incorrect	
			if self.passwords.get(email) != password:
				raise ValueError("Password incorrect!") 

			# password is correct, give a login message, return true		
			if self.passwords.get(email) == password:
				print(f"{email} successfully login!")
				return True
		# except error and give error message
		except ValueError as ex:
			print(ex)
			return False


	def change_password(self, email, password, new_password):
		"""
		let the user input email, password, and new password to change the password

		key attributes:

		email -- a string of email

		password -- a string of old password	

		new_password -- a string of new password			

		"""
		# use try-except construct to catch errors
		try:
			# raise an error if new password is not valid
			if not self.valid_password_len(new_password):
				raise ValueError("Password should be at least 8 characters") 			
			
			# raise an error if failed to login
			if self.login(self, email, password):
				self.passwords[email] = new_password
		# except error and give error message
		except ValueError as ex:
			print(ex)	
	
	
	def delete_account(self, email, password):
		"""
		let the user input email, and password to delete the account

		key attributes:

		email -- a string of email

		password -- a string of password	

		"""
		# use try-except construct to catch errors
		try:
			# login successfully
			if self.login(email, password):
				# delete account from set emails
				self.emails.remove(email)

				# delete account from dictionary passwords
				del self.passwords[email]
				print(f"successfully delete account {email}!")
			# raise an error if failed to login
			else :
				raise ValueError("Failed to login")
		# except error and give error message
		except ValueError as ex:
			print(ex)