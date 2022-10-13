'''
Created on 2022. 10. 7.

@author: zhfld
'''
odd_list = [num for num in range(20) if num%2==1]

chars = 'abcdefghijklmnopqrstuvwxyz';
ascii_alphabet = {letter:chars.index(letter)+97 for letter in chars}

for letter in ascii_alphabet.keys():
    print(letter,':', ascii_alphabet[letter]);
