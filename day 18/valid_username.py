import re
def is_valid(username):
    pattern=r'[a-z][a-z0-9_]{5,11}$'
    if re.match(pattern,username):
        return True
    else: 
        return False
word=input()
print(is_valid(word))