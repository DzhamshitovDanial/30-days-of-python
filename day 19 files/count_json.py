import json
def most(data):
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

def most_populated_countries(data):
    sorted_population=sorted(data,key=lambda x:x['population'],reverse=True)
    print(sorted_population)
    lst=[]
    for i in sorted_population:
        lst.append({
            'country': i['name'],
            'population': i['population']
        })
    n=int(input())
    jsonlst=(lst[:n])
    print(json.dumps(jsonlst,indent=4))



with open('day 19 files\countries_data.json','r') as f:
    data=json.load(f)
most_populated_countries(data)