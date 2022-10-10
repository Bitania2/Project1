import json

stuff = {101: {"item": "chair", "amount": 4,}, 
		 102: {"item": "bed", "amount": 2},
		 103: {"item": "tables", "amount": 4},	 
		 104: {"item": "sofa", "amount": 3},
		 105: {"item": "tv", "amount": 1},
}

js = json.dumps(stuff)
js

fd = open("data.json", 'w')
 
fd.write(js)
fd.close() 

import string

def main(): 
	print(" Home Inventory")
	
	while (1):
		print("1)Display Inventory")
		print("2)Add items to active Inventory")
		print("3)Search Inventory")
		print("4)Exit")
		print("Enter Your Choice :- ")

		n= int(input())
		if (n == 1):
			display_inventory()
			print(stuff)
		elif (n == 2):
			add_items()
		elif (n == 3):
			search_inventory()
		elif (n == 4):
			break
		else:
			print("Error!")


def display_inventory():
 
    fd = open("data.json", 'r')
    txt = fd.read()
    data = json.loads(txt)
     
    fd.close()
    print("Enter '1' To Display Full Inventory")
    n = int(input()) 



def add_items():

	fd = open("data.json", 'r')
	txt = fd. read()
	data = json.loads(txt)


	fd.close()
	print("Enter '2' to add items to active inventory")
	n = int(input())



def search_inventory():

	fd = open("data json", 'r')
	txt = fd. read()
	data = json.loads(txt)



	fd.close()
	print("enter '3' to search inventory")
	n = int(input())








if __name__ == '__main__':
	main()
	
