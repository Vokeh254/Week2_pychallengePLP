#inputs = list of words
#variables = words,my_list, odd_list
#process = create a new list ud=sing list comprehension
#output = a list of words with odd no. of characters

words = input("Enter fours words separated with spaces: ").split()
word1, word2, word3, word4 = words[0], words[1],words[2],words[3]

my_list = [word1, word2, word3, word4]
odd_list = [word for word in my_list if len(word) % 2 != 0]
print(odd_list)