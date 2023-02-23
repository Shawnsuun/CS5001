class Admin_management:


	def __init__(self, admin = set()):
		"""
		constructor of class Admin

		key attributes:

		admin -- a set saving all the admin password

		"""        
		self.admin = admin
		# initialize the admin password as "admincode"
		admin.add("admincode")


	def admin_login(self, admin_pass):
		"""
		let admin login by admin password

		key attributes:

		admin_pass -- password for admin, which is "admincode"

		""" 
		# use try-except construct to catch errors       
		try:
			# raise an error if admin password is not valid
			if admin_pass not in self.admin:
				raise ValueError("Admin password incorrect!") 
			return True
		# except error and give error message
		except ValueError as ex:
			print(ex)
			return False