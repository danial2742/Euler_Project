
import math 

"""
Problem Description Link: https://projecteuler.net/problem=4

Problem Description:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

# Gather our code in a main() function
def main(number):

	print(number)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':

	try:
		number = int(input('Please enter a number: '))
	except Exception as e:
		print('Your Input is not valid. (Used Default Value: 10)')
		number = 10

	main(number)
