"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

dictionary = []
count = 0


def main():
	"""
	TODO:
	"""
	# first_row_letters = ['f', 'y', 'c', 'l']
	# second_row_letters = ['i', 'o', 'm', 'g']
	# third_row_letters = ['o', 'r', 'i', 'l']
	# fourth_row_letters = ['h', 'j', 'h', 'u']
	# all_row_letters = [first_row_letters, second_row_letters, third_row_letters, fourth_row_letters]
	first_row = []
	second_row = []
	third_row = []
	fourth_row = []
	all_row_letters = []

	while True:
		first_row_letters = input('1 row of letters: ' + str())
		for ch in first_row_letters:
			ch = ch.lower()
			first_row.append(ch)
		first_row.pop(1)
		first_row.pop(2)
		first_row.pop(3)
		if not check_legal(first_row):
			print('Illegal input')
			break
		second_row_letters = input('2 row of letters: ' + str())
		for ch in second_row_letters:
			ch = ch.lower()
			second_row.append(ch)
		second_row.pop(1)
		second_row.pop(2)
		second_row.pop(3)
		if not check_legal(second_row):
			print('Illegal input')
			break
		third_row_letters = input('3 row of letters: ' + str())
		for ch in third_row_letters:
			ch = ch.lower()
			third_row.append(ch)
		third_row.pop(1)
		third_row.pop(2)
		third_row.pop(3)
		if not check_legal(third_row):
			print('Illegal input')
			break
		fourth_row_letters = input('4 row of letters: ' + str())
		for ch in fourth_row_letters:
			ch = ch.lower()
			fourth_row.append(ch)
		fourth_row.pop(1)
		fourth_row.pop(2)
		fourth_row.pop(3)
		if not check_legal(fourth_row):
			print('Illegal input')
			break

		all_row_letters.append(first_row)
		all_row_letters.append(second_row)
		all_row_letters.append(third_row)
		all_row_letters.append(fourth_row)

		read_dictionary()
		num_ans = choose_starting_letter(all_row_letters, '', [])
		print('There are ' + str(num_ans) + ' words in total.')
		break


def check_legal(row_letters):
	if len(row_letters) != 4:
		return False

	for ele in row_letters:
		if ele not in ALPHABET:
			return False
	return True


def choose_starting_letter(all_rows_target, ans, chosen_position):
	global count
	# (x, y) is the starting point
	for x in range(0, 4):
		for y in range(0, 4):
			ans += str(all_rows_target[x][y])
			chosen_position.append((x, y))
			count = find_words(all_rows_target, ans, chosen_position, [], x, y)
			ans = ''
			chosen_position = []
	return count


def find_words(all_rows_target, ans, chosen_position, chosen_word, x, y):
	global count
	if has_prefix(ans):
		for i in range(-1, 2):
			for j in range(-1, 2):
				# to ensure not jumping out the bound
				if 0 <= (x + i) <= 3 and 0 <= (y + j) <= 3:
					if (x + i, y + j) not in chosen_position:
						ans += all_rows_target[x + i][y + j]
						chosen_position.append((x + i, y + j))
						# base case!!
						# however, we have to keep searching under this base case.
						if len(ans) >= 4 and ans in dictionary:
							if ans not in chosen_word:
								chosen_word.append(ans)
								print('Found ' + str(ans))
								count += 1
								find_words(all_rows_target, ans, chosen_position, chosen_word, x + i, y + j)
								chosen_position.pop()
						else:
							find_words(all_rows_target, ans, chosen_position, chosen_word, x + i, y + j)
							ans = ans[:len(ans) - 1]
							chosen_position.pop()
	else:
		ans = ans[:len(ans) - 1]
	return count

def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
