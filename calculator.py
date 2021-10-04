import re #here we are importing regex

print("Calculator") #printing calculator
print("Type quit to exit\n") #telling user how to quit the cal

prev=0 #prev is variable where its is used asstore the calculated values

run=True #it s used for looping

def performMath(): #function of calculator
	global run		#making these as global variables so that there wont be errors about being local variable scpe
	global prev
	eq=''	#defininh eq variable
	if prev==0:	#taking inout into prev for the first time
		eq=input("enter equation : ") #taking input into eq variable
	else:	#taking input if its not first time
		eq=input(str(prev)) #taking prev variable as input into eq
	if eq == 'quit':	#using quit to close the calculator
		 run=False	#breaking the loop by making while as false
	else:	#if user dont want to quit and wanted do some performations
		eq=re.sub('[a-z A-Z,.()" "@#$]','',eq) 
		"""using regex to remove all alphabets and some symbols other 
		than mathematicak opertaion so that it 
		wont be problemcause the eval() function
		 is very dangerous with that on
		  ecan crash their system"""
		if prev==0: #for the fist time
			prev= eval(eq) #evalating eq using eval() function
		else: #if its not first time
			prev=eval(str(prev)+eq) #evalating the eq with including previous result an dstroing it into prev variable
		print("The result is : ",prev) #printing the calculated value

while run:
	performMath()
