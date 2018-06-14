from retailitem import RetailItem

def main():
	item_1 = RetailItem("Jacket", "12", "$59.95")
	item_2 = RetailItem("Designer Jeans", "40", "$34.95")
	item_3 = RetailItem("Shirt", "20", "$24.95")
	item_list = [item_1, item_2, item_3]
	item_number = 1
	for item in item_list:
		print("Retail Item "+ str(item_number) + ":")
		print("Description: ", item.description)
		print("Units in inventory: ", item.inventory)
		print("Price: ", item.price, '\n')
		item_number = item_number + 1
main()

