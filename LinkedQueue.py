class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, max_size=None):
        self.front = self.rear = None
        self.size = 0
        self.max_size = max_size  # optional limit

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return self.max_size is not None and self.size >= self.max_size

    def enqueue(self, data):
        if self.is_full():
            print("Overflow: Queue is full")
            return
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Inserted {data}")

    def dequeue(self):
        if self.is_empty():
            print("Underflow: Queue is empty")
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Deleted {temp.data}")
        return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
