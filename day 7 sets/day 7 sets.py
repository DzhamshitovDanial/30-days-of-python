def exercise1():
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    print(len(it_companies))
    it_companies.add('Twitter')
    print(it_companies)
    bonus_companies = {'Samsung','Xiamomi','Netflix'}
    it_companies.update(bonus_companies)
    print(it_companies)
    it_companies.remove('Twitter')
    print(it_companies)
def exercise2():
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    print(A.union(B))
    print(A.intersection(B))
def exercise3():
    age = [22, 19, 24, 25, 26, 24, 25, 24]
    age_set=set(age)
    print(len(age))
    print(len(age_set))