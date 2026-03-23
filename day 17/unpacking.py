def analyze_data(args):
    first,*middle,last=args
    print(f'First:{first},Middle:{middle},last:{last}')
n=int(input('How many?-'))
s=[]
for i in range(n):
    a=int(input())
    s.append(a)
analyze_data(s)