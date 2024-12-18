

data = []
indices = {}

def insert(val):
    if val not in indices:
        data.append(val)
        indices[val] = len(data)-1
        return True 
    else:
        return False

print(insert(4))





