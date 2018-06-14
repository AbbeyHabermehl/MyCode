class RetailItem:
	def __init__(self, description, inventory, price):
		self.description = description
		self.inventory = inventory
		self.price = price
	def return_description(self):
		return self.description
	def return_inventory(self):
		return self.inventory
	def return_price(self):
		return self.price
	def __str__(self):
		result = 'Description: ' + self.description + '\n' + \
		'Units in inventory: ' + str(self.inventory) + \
		'\nPrice: $' + str(self.price)
		return result
