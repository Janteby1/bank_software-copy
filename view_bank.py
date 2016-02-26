# bank app (MVP)
import sys

class View ():

	def welcome (self):
		print ("")
		print ("Welcome to the bank app!")
		print ("As a client you can log in, see you balances, make a withdrawl or deposit and even transfer funds.")
		print ("There is also an option to log in as a banker with secured credentials.")
		print ("Lets get started ... ")
		print ("")

	def signup_name (self):
		while True:
			print (" ")
			self.name = input ("What is your name: ")
			if self.name.isalpha() == True:
				break
			print ("Please enter only alpha characters")
		return self.name

	def signup_username(self):
		while True:
			print (" ")
			self.username = input ("Please create username: ")
			if self.username.isalpha() == True:
				break
			print ("Please enter only alpha characters")
		return self.username

	def signup_password (self):
		while True:
			print (" ")
			self.password = input ("Please create password: ")
			if self.password.isalpha() == True:
				break
			print ("Please enter only alpha characters")
		return self.password

	def login_username(self):
		print ("")
		self.name = input ("What is your name: ")
		self.username = input ("Please enter your username: ")
		return self.username

	def login_password(self):
		self.password = input ("Please enter your password: ")
		return self.password

	def restart(self):
		print("")
		print ("Great! You created an act.")
		print ("Please restart and log back in.")
		print ("Thank you")

	def check_permission(self):
		self.user = input ("Are you a banker or a client? ")
		return self.user

	def choice(self):
		self.choice = input ("Do you want to sign up [1] or log in [2]?" )
		return self.choice

	def try_again (self):
		print ("We coult not find your username or password, please try again")

	def choice_bal (self):
		choice = input ("Enter 1 to see your all balances attached to that act or 2 to skip: ")
		return choice

	def get_act (self):
		print("")
		userid = input ("Please enter your Act number: ")
		return userid

	def print_bal (self, balances):
		print ("Balances: $", balances)















