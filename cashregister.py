
class CashRegister:
	def __init__(self):
		self.checkout_cart = [] # List of type RetailItem
	def purchase_item(self, purchased_item):
		self.checkout_cart.append(purchased_item)

	def get_total(self):
		total = 0
		for item in self.checkout_cart:
			total = item.price + total
		return total 

	def show_items(self):
		for item in self.checkout_cart:
			print(item)
			print()

	def clear(self):
		del self.checkout_cart[:]
		# could also do:
		# self.checkout_cart = []

