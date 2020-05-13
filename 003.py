import math 

"""
Problem Description Link: https://projecteuler.net/problem=3

Problem Description:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

# Gather our code in a main() function
def main(n):
	primes_factor = dict()
	# Print the number of two's that divide n 
	while n % 2 == 0:

		if 2 in primes_factor:
			primes_factor[2] += 1
		else:
			primes_factor[2] = 1

		n = n / 2
		  
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 
		  
		# while i divides n , print i ad divide n 
		while n % i== 0: 

			if i in primes_factor:
				primes_factor[i] += 1
			else:
				primes_factor[i] = 1

			n = n / i
			  
	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		if n in primes_factor:
			primes_factor[n] += 1
		else:
			primes_factor[n] = 1

	print(primes_factor)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':

	try:
		number = int(input('Please enter a number: '))
	except Exception as e:
		print('Your Input is not valid. (Used Default Value: 10)')
		number = 10

	main(number)
