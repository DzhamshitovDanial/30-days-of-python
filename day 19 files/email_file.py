import re
import json
def sorted_list(x):
    sorted_list=sorted(x,key=lambda x:x['emails'])
    return sorted_list
with open('30-days-of-python\day 19 files\email_exchanges_big.txt','r') as f:
    data=f.read()
pattern_email=r'[a-zA-Z.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
all_emails=re.findall(pattern_email,data)
unique_emails=set(all_emails)
unique_emails_lst=[]
for i in unique_emails:
    unique_emails_lst.append({
        'emails':i
    })

print(json.dumps(sorted_list(unique_emails_lst),indent=1))