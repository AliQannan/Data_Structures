class NodeD:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=' <-> ')
            current = current.next
        print('None')

    def print_backward(self):
        current = self.head
        if not current:
            print('None')
            return
        while current.next:
            current = current.next
        while current:
            print(current.value, end=' <-> ')
            current = current.prev
        print('None')

    def insert_front(self, value):
        new_node = NodeD(value)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = NodeD(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def remove_by_value(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert_before(self, index, value):
        new_node = NodeD(value)
        if index == 0:
            return self.insert_front(value)
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        if not current:
            print("Index out of bounds.")
            return
        previous = current.prev
        previous.next = new_node
        new_node.prev = previous
        new_node.next = current
        current.prev = new_node

    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        seen = set()
        current = self.head
        while current:
            if current.value in seen:
                prev_node = current.prev
                next_node = current.next
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                if current == self.head:
                    self.head = next_node
            else:
                seen.add(current.value)
            current = current.next
