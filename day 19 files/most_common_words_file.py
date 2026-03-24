def most_common_word(file,n):
    words_list={}
    words=file.split()
    for word in words:
        if word in words_list:
            words_list[word]+=1
        else:
            words_list[word]=1
    words_list_sorted=sorted(words_list.items(),key=lambda x:x[1],reverse=True)
    print(words_list_sorted[:n])
            

file_path='day 19 files\obama_speech.txt'
with open(file_path,'r') as f:
    file=f.read()
n=int(input('How many words'))
most_common_word(file,n)