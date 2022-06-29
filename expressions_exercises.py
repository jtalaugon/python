#!/usr/bin/python3
# Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9)
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))
# Write a Python program that matches a string that has an "a" followed by zero or more b's.
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))
print(text_match("baa"))
# Write a Python program that matches a string that has an a followed by one or more b's.
def match_string(text):
    match = 'b'
