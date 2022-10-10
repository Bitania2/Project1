
#create fn
Stuff = {'chairs': 4, 'beds': 2, 'tables': 4, 'sofas': 3, 'TV': 1}
print(Stuff);

inputs = input('Welcome to the inventory Editor \n Press 1 to read stuff \n Press 2 to Save \n Press 3 Display\n press 4 to search \n ')

if int(inputs)==1:
	print(Stuff)
if int(inputs)==2:
	inputItemName=input("Put in item name\n")
	inputItemNumber=input("Put in item number\n")
	Stuff.update({inputItemName: int(inputItemNumber)})
	print(Stuff)
if int(inputs)==4:
	inputKeyName=input("Put in Key ")
	if inputKeyName in Stuff:

		print (inputKeyName, Stuff[inputKeyName])

					
  		  

 	

	


