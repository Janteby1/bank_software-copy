import sqlite3
db = 'bank.db'
import pudb 

connection = sqlite3.connect(db)
c = connection.cursor()

class Model:
	# no init function, all the attributes are given using input statments   
	def create_user(self, name, username, password, permission):
		c.execute("""
	        INSERT INTO users ("name", "username", "password", "permission") VALUES (?, ?, ?, ?)""",(name, username, password, permission))
		connection.commit()

	def print_user(self):
		cursor = connection.execute("SELECT name, username, password, permission FROM users")
		i =0
		while i < 1:
			for row in cursor:
				print (" ")
				print (" --- DATABASE ---")
				print ("Users")
				print ("NAME = ", row[0])
				print ("USERNAME = ", row[1])
				print ("PASSWORD = ", row[2])
				print ("PERMISSION = ", row[3], "\n")
			i +=1

	def check_login(self, username, password):
		info_list = []
		info_list = c.execute("""
			SELECT id FROM users WHERE username = ? AND password = ?""", (username, password))
		connection.commit()
		return info_list.fetchone() 

	def check_balance(self, userid):
		balances = []
		balances = c.execute("""
			SELECT acttype, balance FROM acts WHERE userid = ? """, (userid,))
		return balances.fetchall() 
		connection.commit()

	def choose_act(self, userid):
		acts = []
		acts = c.execute("""
			SELECT acttype FROM acts WHERE userid = ? """, (userid,))
		return acts.fetchall() 
		connection.commit()

	def deposit(self, userid, acttype, balance):
		c.execute("""
			UPDATE acts SET balance = (balance + ?) WHERE userid = ? AND acttype = ?""", (balance, userid, acttype))
		connection.commit()
		print ("Funds added")
		print("")

	def withdraw(self, userid, acttype, balance):
		c.execute("""
			UPDATE acts SET balance = (balance - ?) WHERE userid = ? AND acttype = ?""", (balance, userid, acttype))
		connection.commit()
		print ("Funds withdrawn")
		print("")


	# still not acctually changing funds
	def transfer(self, userid, acttype, acttype2, balance):
		# pu.db
		c.execute("""
			UPDATE acts SET balance = (balance - ?) WHERE userid = ? AND acttype = ?""", (userid, acttype, balance))
		c.execute("""
			UPDATE acts SET balance = (balance + ?) WHERE userid = ? AND acttype = ?""", (userid, acttype2, balance))
		connection.commit()
		print ("Funds transfered")
		print("")





