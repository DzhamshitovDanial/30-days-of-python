class statistics:
    def __init__(self,ages):
        self.count=len(ages)
        self.sum=sum(ages)
        self.min=min(ages)
        self.max=max(ages)
    def data_describe(self):
        return self.count,self.sum
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data=statistics(ages)
print(data.count)
print(data.data_describe())