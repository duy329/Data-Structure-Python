class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return False
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        temp = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.value
    
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp