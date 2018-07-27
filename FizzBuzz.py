# FizzBuzz solution by Jack Wilburn

for i in range(1,101):
	a = i % 3
	b = i % 5
	string = ''

	if a == 0:
		string += "Fizz"
	if b == 0:
		string += "Buzz"

	print(string or i)