import re
word=input()
pattern=r'\w+'
regword=re.findall(pattern,word)
print(regword)
most=''
mx=0
for i in range(len(regword)):
    word_count=regword.count(regword[i])
    print(word_count)
    if word_count>mx:
        mx=word_count
        most=regword[i]
print(most)