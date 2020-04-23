class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other.data:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other.data:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:
    
    def issubset(self, other):
        for x in self.data:
            if not x in other.data: 
                return False
            if x in other.data:
                continue
        return True
    
    def issuperset(self, other):
        for x in other.data:
            if not x in self.data:
                return False 
            if x in self.data:
                continue
        return True
        
    def intersection_update(self, other):
        for x in self.data:
            if not x in other.data:            
                self.data.append(x)
        return self.data
    
    def difference_update(self, other):
        for x in self.data:
            if x in other.data:            
                self.data.remove(x)
        return self.data
    
    def symmetric_difference_update(self, other):
        res = []
        for y in other.data:
            if y in self.data:     
                res.append(y)
            if not y in self.data:
                self.data.append(y)
        for x in res:
            if x in self.data:
                self.data.remove(x)
        return self.data
    
    def add(self, elem):
        for y in elem.data:
            self.data.append(y)
        return self.data
    
    def remove(self, elem):
        for y in elem.data:
            if not y in self.data:
                raise KeyError('elem is not contained in the set')
            if y in self.data:
                self.data.remove(y)
        return self.data
             
x=Set([1,2])
y=Set([1,2,3,4,5,6])

print(x.issubset(y))
print(x.issuperset(y))
print(x.intersection_update(y))
print(x.difference_update(y))
print(x.symmetric_difference_update(y))
print(x.add(y))
print(x.remove(y))