from retailitem import RetailItem
from cashregister import CashRegister


def get_user_choice():
	menu = ['Pants', 'Shirt', 'Dress', 'Socks', 'Sweater']
	print("Menu")
	print('------------------------------')
	for i in range(len(menu)):
		print(str(i + 1)+ '. ' + menu[i])
	print()

	choice = int(input('Enter the menu number of the item' + \
						' you would like to purchase: '))
	print()
	#while loop to make sure a valid number is chosen
	while choice < 1 or choice > len(menu):
		choice = int(input('Please enter a valid item number: '))
		print()
	return choice


# main method
def main():
	# create sale items
	
    pants = RetailItem('Pants', 10, 19.99)
    shirt = RetailItem('Shirt', 15, 12.50)
    dress = RetailItem('Dress', 3, 79.00)
    socks = RetailItem('Socks', 50, 1.00)
    sweater = RetailItem('Sweater', 5, 49.99)

    # Create dictionary to pair item with selection number
    menu_dict = {1: pants, 2: shirt, 3: dress, 4: socks, 5: sweater}
    register = CashRegister()
    # keep prompt running until user is done enterring
    done = 'N'
    #user wants to purchase more items:
    while done == 'N':
    	user_choice = get_user_choice()
    	item = menu_dict[user_choice]
    	if item.inventory == 0:
    		print('The item is out of stock.')
    	else:
    		register.purchase_item(item)
    		item.inventory = item.inventory - 1
    		print('item was added to the cash register.')
    		done = input('Are you ready to check out (Y/N)? ')
    		print()
    print('Your purchase total is: ', register.get_total())
    print()
    print('The items in the cash register are: ')
    print()
    register.show_items()


main()