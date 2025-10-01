class account:
	def __init__(self,bal,acc_no):
		self.bal = bal
		self.acc_no = acc_no
	def debits(self,ammount):
		self.bal -= ammount
		print("BAT",ammount,"Was debited")
		print("Total balance = ",self.get_bal())
		
	def cradits(self,ammount):
		self.bal += ammount
		print("BAT",ammount,"Was creadited")
		print("Total balance = ",self.get_bal())
		
	def get_bal(self):
		return self.bal
		
acc1 = account(10000,123)
acc1.debits(100)
acc1.cradits(500)