def reverse_string(s):
	rev = ""
	for i in range(len(s)- 1, -1, -1):
		rev += s[i]
	return rev 

def fibonacci(n):
	if n <= 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)
		
def fib_iter(n):
	if n <= 1:
		return 1
	else:
		fib_n1 = 1
		fib_n2 = 1

		for i in range(n-2):
			tmp = fib_n2
			fib_n2 += fib_n1
			fib_n1 = tmp 
		return fib_n1 + fib_n2 

def mult_table(n):
	# Prints out the multiplication table up to n X n 
	row = ""
	for i in range(1, n+1):
		for j in range(1, n+1):
			row += " " + str(i*j).rjust(3)
		print(row)
		row = ""

def sum_ints(file):
	# Write a function that sums integers from a text file, one int per line
	sum = 0
	try:
		f = open(file, "r")
		f1 = f.readlines()
		
		for line in f1:
			sum += int(line)
	except FileNotFoundError:
		print("File not found")
	return sum 
	
def print_odd(n):
	# Print the odd numbers from 1 to n
	for i in range(1, n+1):
		if i % 2 != 0:
			print(i)

def largest_int(arr):
	# Find the largest integer within an array
	if len(arr) == 1:
		return arr[0]
	
	largest = 0
	for i in arr:
		largest = max(i, largest)
	return largest 

def format_rgb(r, g, b):
	# Format an RGB value as a 6-digit hex string 
	return hex(r).split("0x")[1] + hex(g).split("0x")[1] + hex(b).split("0x")[1]