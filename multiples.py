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

# Print multiples
for x in range(1, 11):
	print("{} times {} is equal to {}.".format(x, numb, (x * numb)))