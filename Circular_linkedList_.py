class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def insert_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_after(self, index, value):
        if not self.head:
            print("List is empty.")
            return
        new_node = Node(value)
        current = self.head
        i = 0
        while i < index and current.next != self.head:
            current = current.next
            i += 1
        new_node.next = current.next
        current.next = new_node

    def remove_by_value(self, value):
        if not self.head:
            return
        current = self.head
        prev = None
        while True:
            if current.value == value:
                if current == self.head:
                    # find tail
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head.next == self.head:
                        self.head = None
                        return
                    tail.next = self.head.next
                    self.head = self.head.next
                    return
                else:
                    prev.next = current.next
                    return
            prev = current
            current = current.next
            if current == self.head:
                break

    def remove_duplicates(self):
        if not self.head or self.head.next == self.head:
            return
        seen = set()
        current = self.head
        prev = None
        first_pass = True
        while True:
            if current.value in seen:
                prev.next = current.next
                if current == self.head:
                    self.head = current.next
            else:
                seen.add(current.value)
                prev = current
            current = current.next
            if current == self.head:
                if first_pass:
                    first_pass = False
                else:
                    break

    def search(self, value):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

    def to_list(self):
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break
        return result
