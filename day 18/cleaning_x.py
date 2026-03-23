import re
word=input()
pattern=r'[^a-zA-z-Zа-яА-Я0-9/s]'
regword=re.sub(pattern,'\n',word)
print(regword)