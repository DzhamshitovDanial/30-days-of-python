names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
studens_and_scores=[]

for n,s in zip(names,sorted(scores,reverse=True)):
    studens_and_scores.append(f'{n}: {s}')
for index,ss in enumerate(studens_and_scores):
    print(index+1,ss)

