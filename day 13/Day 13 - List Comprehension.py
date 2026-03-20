numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst=[i for i in numbers if i<=0]
print (lst)
#
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst=[j for i in list_of_lists for j in i]
print(lst)
#
lst=[(i,i**0  ,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(*lst,sep='\n')
#
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst=[{'country': j[0],'city': j[1]} for i in countries for j in i]
print(lst)