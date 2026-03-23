import re
word=input()
pattern=r'\b[п][а-яё]*'
regword=re.findall(pattern,word,re.I)
print(regword)