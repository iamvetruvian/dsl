class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]
        self.SENTINEL = object()  # sentinel for deleted elements
    
    def getHash(self, key):
        return key % self.size
    
    def insert(self, key, value):
        h = self.getHash(key)

        # If empty or deleted slot at hash position
        if self.table[h] is None or self.table[h] == self.SENTINEL:
            self.table[h] = [key, value]
            return

        # If updating existing key
        if self.table[h][0] == key:
            self.table[h][1] = value
            return

        # Linear probing
        idx = (h + 1) % self.size
        while (self.table[idx] is not None and
               self.table[idx] != self.SENTINEL and
               self.table[idx][0] != key):
            idx = (idx + 1) % self.size
            if idx == h:
                print("Table is full!")
                return

        self.table[idx] = [key, value]
    
    def delete(self, key):
        h = self.getHash(key)

        # Start probing
        idx = h
        while self.table[idx] is not None:
            if self.table[idx] != self.SENTINEL and self.table[idx][0] == key:
                self.table[idx] = self.SENTINEL
                print(f"Deleted {key}")
                return
            idx = (idx + 1) % self.size
            if idx == h:
                break
        print("Element not found!")
    
    def display(self):
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")

# Example usage
ht = HashTable(5)
ht.insert(10, "Apple")
ht.insert(15, "Banana")
ht.insert(20, "Cherry")
ht.display()
ht.delete(15)
ht.insert(25, "Mango")  # should reuse deleted slot
ht.display()
