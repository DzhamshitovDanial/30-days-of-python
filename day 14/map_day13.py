def uppper_case(x):
    return x.upper()
def square(x):
    return x**2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(uppper_case, countries)
print(list(result))
print(list(map(square,numbers)))
