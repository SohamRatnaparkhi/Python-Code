class HashTable:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size
        
    def get_valid_index(self, key):
        # returns empty index and also find index of key
        i = hash(key) % len(self.data_list)
        while(True):
            kv = self.data_list[i]
            if kv is None:
                # For returning valid index
                return i
            
            elif kv[0] == key:
                # For finding
                return i
            
            elif len(self.data_list) == i:
                i = 0

            i += 1
        
    def __getitem__(self, key):
        # Implement the logic for "find" here
        i = self.get_valid_index(key)
        return self.data_list[i]
    
    def __setitem__(self, key, value):
        # Implement the logic for "insert/update" here
        i = self.get_valid_index(key)
        self.data_list[i] = key,value
        pass # change this
    
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        return len([x for x in self])
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)

def input_data():
    size = int(input("Enter size of HashMap - "))
    hashmap = HashTable(size)
    n = int(input("Number of number of elements - "))
    for i in range(0, n):
        inp = input("Key - value pair strictly seperated by spaces - ").strip().split()
        if len(inp) == 2 : hashmap[inp[0]] = inp[1] 
        else: hashmap[inp[0]] = None

    print(hashmap)
    f = input("Enter key whose value is to be found - ")
    print(hashmap[f])

input_data()