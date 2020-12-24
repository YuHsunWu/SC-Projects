"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dictionary = []
num_ans = 0
word_found_lst = []

def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        target = str(input('Find anagrams for: ' + str()))
        if target == EXIT:
            break
        else:
            print('Searching...')
            read_dictionary()
            find_anagrams(target)
            print(str(num_ans) + ' anagrams: ', end=' ')
            print(word_found_lst)



def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    count = 0
    word_resource_lst = []
    for ch in s:
        word_resource_lst.append(ch+str(count))
        count += 1
    find_anagrams_helper(s, '', [], word_resource_lst)


def find_anagrams_helper(s, ans, ans_lst_position, word_resource_lst):
    global word_found_lst, num_ans
    if len(ans_lst_position) == len(s):
        # ans will be like: 'apple'
        for ele in ans_lst_position:
            ans += ele[0]
        if ans in dictionary and ans not in word_found_lst:
            print('Found: ' + str(ans))
            print('Searching...')
            num_ans += 1
            word_found_lst.append(ans)
    else:
        if has_prefix(ans_lst_position):
            # word_resource_list will be like: ['a0', 'p1', 'p2', 'l3', 'e4']
            for element in word_resource_lst:
                if element not in ans_lst_position:
                    ans_lst_position.append(element)
                    find_anagrams_helper(s, ans, ans_lst_position, word_resource_lst)
                    ans_lst_position.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    check = ''
    for ele in sub_s:
        check += ele[0]
    for word in dictionary:
        if word.startswith(check):
            return True
    return False







if __name__ == '__main__':
    main()
