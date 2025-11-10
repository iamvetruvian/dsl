class Node:
    def __init__(self, isbn, author, title):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, isbn, author, title):
        newNode = Node(isbn, author, title)
        if self.root is None:
            self.root = newNode
            return
        else:
            self._insert(self.root, newNode)
    
    def _insert(self, current, newNode):
        if newNode.isbn < current.isbn:
            if current.left is None:
                current.left = newNode
            else:
                self._insert(current.left, newNode)
            return
        if newNode.isbn > current.isbn:
            if current.right is None:
                current.right = newNode
            else:
                self._insert(current.right, newNode)
            return
        if newNode.isbn == current.isbn:
            print("An entry with that ISBN already exists! ISBN should be unique.")
            return
    
    def search(self, isbn):
        return self._search(self.root, isbn)
    
    def _search(self, current, isbn):
        if isbn < current.isbn:
            return self._search(current.left, isbn)
        if isbn > current.isbn:
            return self._search(current.right, isbn)
        if isbn == current.isbn:
            return current
        if current is None: return None
    
    def delete(self, isbn):
        return self._delete(self.root, isbn)

    def _delete(self, current, isbn):
        if current is None: return None
        if isbn < current.isbn:
            current.left = self._delete(current.left, isbn)
        elif isbn > current.isbn:
            current.right = self._delete(current.right, isbn)
        else:
            successor = self._find_min(self, current.right)
            current.isbn = successor.isbn
            current.title = successor.title
            current.author = successor.author
            current.right = self._delete(current.right, successor.isbn)
        return current
        
    def _find_min(self, current):
        assume = current.left
        while assume:
            assume = current.left
        return assume

    #Traversals:
    #Inorder: left - root - right
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, current):
        if current:
            self._inorder(current.left)
            print(current)
            self._inorder(current.right)

    #Pre-order: root - left - right
    def preorder(self):
        self._preorder(self.root)
    
    def _preorder(self, current):
        if current:
            self._preorder(current.left)
            self._preorder(current.right)
            print(current)

    #Post-order: left - right - root
    def postorder(self):
        self._postorder(self.root)
    
    def _postorder(self, current):
        if current:
            print(current)
            self._postorder(current.left)
            self._postorder(current.right)
