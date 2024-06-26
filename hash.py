class Hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self,key):
        return hash(key)%self.size

    def insert(self,key,value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0]==key:
              pair[1]=value
              return
        self.table[index].append([key,value])
    
    def search(self,key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0]==key:
              return pair[1]
    
    def delete(self,key):
        index = self._hash_function(key)
        for i,pair in enumerate(self.table[index]):
            if pair[0]==key:
                del self.table[index][i]
                return
    
ht =Hashtable(5)
ht.insert('apple',1)
ht.insert('banana',2)
ht.insert('orange',3)
ht.delete('orange')
print(ht.search('orange'))