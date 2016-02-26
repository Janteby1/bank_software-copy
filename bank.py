# split into M, V, c files - DONE
# Add database to it with SQL

# bank app (MVP)
import sys
import pudb

from view_bank import View
from model_bank import Model

class User():
	def __init__ (self, name, username, password):
		self.name = None
		self.username = None
		self.password = None

	def __repr__ (self):
		return str(self.value)

class Banker(User):
	def __init__ (self, name ,username, password, permission):
		User.__init__(self, name ,username, password)
		self.permission = None
		self.view = View()
		self.model = Model()

	def signup (self):
		self.name = self.view.signup_name()
		self.username = self.view.signup_username()
		self.password = self.view.signup_password()
		# send the values to the db
		self.model.create_user(self.name, self.username, self.password, self.permission)
		self.view.restart()
		sys.exit()

	def login (self):
		self.username = self.view.login_username()
		self.password = self.view.login_password()
		info_list = self.model.check_login (self.username, self.password)
		if info_list is not None:
			print (info_list)
		else:
			self.view.try_again()
			sys.exit()
			# need to get this to loop

class Client(User):
	def __init__ (self, name ,username, password, permission):
		User.__init__(self, name ,username, password)
		self.permission = 1
		self.view = View()
		self.model = Model()

	def signup (self):
		self.name = self.view.signup_name()
		self.username = self.view.signup_username()
		self.password = self.view.signup_password()
		# send the values to the db
		self.model.create_user(self.name, self.username, self.password, self.permission)
		self.view.restart()
		sys.exit()

	def login (self):
		self.username = self.view.login_username()
		self.password = self.view.login_password()
		info_list = self.model.check_login (self.username, self.password)
		if info_list is not None:
			print ("Act number: ", info_list)
		else:
			self.view.try_again()
			sys.exit()
			# need to get this to loop

	def view_act (self):
		print ("")
		choice = self.view.choice_bal()
		if choice == "1":
			userid = self.view.get_act()
			balances = self.model.check_balance(userid)
			self.view.print_bal(balances)
		else:
			pass

	def funds (self):
		print ("")
		choice = input ("Enter 1 to make a deposit or 2 to withdraw funds (press any other key to skip): ")
		if choice == "1":
			print("")
			userid = input ("You chose to make a deposit. Please enter your Act number: ")
			acts = self.model.choose_act(userid)
			print ("All accounts", acts)
			act = input ("Please choose an act to deposit funds into: ")
			act = act.lower()
			amt = input ("Please choose how much to deposit: ")
			amt = int(amt)
			self.model.deposit(userid, act, amt)
			self.view_act()

		elif choice == "2":
			print("")
			userid = input ("You chose to withdraw funds. Please enter your Act number: ")
			acts = self.model.choose_act(userid)
			print ("All accounts", acts)
			act = input ("Please choose an act to withdraw funds from: ")
			act = act.lower()
			amt = input ("Please choose how much withdraw (be careful not to overdraft): ")
			amt = int(amt)
			self.model.withdraw(userid, act, amt)
			self.view_act()
		else:
			pass

	def transfer (self):
		print ("")
		choice = input ("Enter 1 transfer funds between accounts or press any other key to skip: ")
		if choice == "1":
			print("")
			userid = input ("You chose to transfer funds. Please enter your Act number: ")
			userid = int(userid)
			acts = self.model.choose_act(userid)
			print ("All accounts", acts)
			act = input ("Please choose an act to take funds from: ")
			act = act.lower()
			act2 = input ("Please choose an act to send funds to: ")
			act2 = act2.lower()
			amt = input ("Please choose how much to transfer: ")
			amt = int(amt)
			self.model.transfer(userid, act, act2, amt)
			self.view_act()
		else: 
			pass

class Run ():
	def __init__ (self):
		self.client1 = Client(None,None,None,None)
		self.banker1 = Banker(None,None,None,None)
		self.view = View()

	def permissions (self):
		self.view.welcome()
		user = self.view.check_permission()
		user = user.lower()

		if user == "client":
			choice = self.view.choice()
			if choice == "1":
				self.client1.signup()
			elif choice == "2":
				self.client1.login()
			else:
				self.permissions() 

		elif user == "banker":
			choice = self.view.choice()
			if choice == "1":
				self.banker1.signup()
			elif choice == "2":
				self.banker1.login()
			else:
				self.permissions()

		else:
			self.permissions()

	def choose_action (self):
		self.client1.view_act()
		self.client1.funds()
		self.client1.transfer()

run1 = Run()
run1.permissions()
# run1.printer()
run1.choose_action()

