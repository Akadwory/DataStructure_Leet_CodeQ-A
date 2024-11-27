import random 


class RandomizedSet:
    def __init__(self):
        self.data = []
        self.indices = {}

    def insert(self,val):
        if val in self.indices:
            return False
        else:
            self.data.append(val)
            self.indices[val] = len(self.data) - 1 
            return True,self.data

x = RandomizedSet()
print(x.insert(4))
print(x.insert(2))
print(x.insert(4))

        


