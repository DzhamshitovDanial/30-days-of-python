with open('30-days-of-python\day 19 files\obama_speech.txt','r') as file:
    lines=file.readlines()
    print(len(lines))
    text=''.join(lines)
    words=text.split()
    print(len(words))