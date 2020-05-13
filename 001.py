import sys

"""
Problem Description Link: https://projecteuler.net/problem=1

Problem Description:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""


# Gather our code in a main() function
def main(to):
	conditions = lambda x: x % 3 == 0 or x % 5 == 0

	numbers = list(filter(conditions, range(to)))

	Sum = sum(numbers) 

	print('Total:', Sum) 



# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':

	try:
		# Command line args are in sys.argv[1], sys.argv[2] ..
		# sys.argv[0] is the script name itself and can be ignored
		to = int(sys.argv[1])
	except:
		print('Your Input is not valid. (Used Default Value: 10)')
		to = 10

	main(to)
