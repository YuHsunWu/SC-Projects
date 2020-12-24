"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

largest_digit = 0

def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	global largest_digit
	if n < 0:
		n = -n
	largest_digit = 0
	find_largest_digit_helper(n)
	return largest_digit


def find_largest_digit_helper(n):
	global largest_digit
	if n < 1:
		return largest_digit
	else:
		new_digit = int((n / 10 - int(n / 10)) * 10)
		if new_digit > largest_digit:
			largest_digit = new_digit
		find_largest_digit_helper(n/10)





if __name__ == '__main__':
	main()
