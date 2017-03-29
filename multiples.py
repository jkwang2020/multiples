# Get number
numb = input("Give me a number: ")

# Cast to float
valid = False
while valid == False:
	try:
		numb = float(numb)
		valid = True
	except:
		numb = input("That wasn't a number! Try again: ")

# Double it
numb *= 2

# Print result
print("Double your number is " + str(numb))