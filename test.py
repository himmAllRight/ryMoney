import datetime

class Node:
	def __init__(self, inDate):
		dateString = inDate.split("/")
		print(dateString)
		self.date = datetime.date(int(dateString[2]),int(dateString[0]),int(dateString[1]))

		self.date = self.date.strftime("%m/%d/%y")

		print(self.date)




birthday = "09/06/1991"
newDay   = "01/11/1995"

node1 = Node(birthday)
node2 = Node(newDay)


class Test:
	def __init__(self, testDate):
		dateString = testDate.split("/")
		date = datetime.date(int(dateString[2]),int(dateString[0]),int(dateString[1]))
		
		print(date)
		print(node1.date)
		print(node2.date)

		if(date > node1.date):
			print("1")
		if( date < node2.date):
			print("2")
		if(date > node1.date and date < node2.date):
			print("3")
		else:
			print("haha")

Test("10/14/1991")