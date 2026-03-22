def average(a,b,c,d,e):
    return (a+b+c+d+e)/5
n=int(input('how man digits?-'))
lst=[]
for i in range(n):
    digit=int(input())
    lst.append(digit)
try:
    print(average(*lst))
except ValueError:
    print('vayle error')
except TypeError:
    print('type error')
finally:
    print('All done')