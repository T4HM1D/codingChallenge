#Coding Challenge 1:SPY number finder

sumNum = 0 #global variable counter for sum
product = 1 #global variable counter for product
def sp(number): #Recursive function
	global sumNum
	global product
	
	if(number > 0): # function stops once all digits been used
		reminder = number % 10 #stores each last digit of number
		sumNum = sumNum + reminder #adds last digit to counter
		product = product * reminder #multiply last digit to counter
		sp(number // 10) #recursively calls itself by removing last digit	
	elif(sumNum == product): # compares sum and product of digits
		print("sum of digits: " + str(sumNum))
		print("product of digits: " + str(product))
		print("sum and product of digits the given number are equal therefore is a SPY number.") #if equal number is SPY number
	else:
		print(str(sumNum) + " and " + str(product) + " are not equal therefore given number is not SPY number.") #if not equal, number is not SPY number

n = int(input("enter number > 0: "))#takes use input, must be positive integer
sp(n)	
