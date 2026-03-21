def land(x):
    if 'land' in x:
        return True
    return False

def six_charcters(x):
    if len(x)==6:
        return True
    return False
def e_start(x):
    if x[0].upper()=='E':
        return True
    return False

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(land,countries)))
print(list(filter(six_charcters,countries)))
print(list(filter(e_start,countries)))