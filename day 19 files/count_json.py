import json
def most():
    with open('30-days-of-python\day 19 files\countries_data.json','r') as f:
        data=json.load(f)

    all_languages=[]
    for i in range(len(data)):
        all_languages.extend(data[i]['languages'])

    most_spoken={}
    for j in all_languages:
        if j in most_spoken:
            most_spoken[j]+=1
        else:
            most_spoken[j]=1
    sorted_list=sorted(most_spoken.items(), key=lambda x:x[1], reverse=True)
    n=int(input())
    print(sorted_list[:n],sep='\n')

most()