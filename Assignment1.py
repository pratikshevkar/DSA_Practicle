
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        print(" ".join(values))

    def insert(self, data, position):
        if position < 0:
            return

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                return
            current = current.next

        if current is None:
            return

        new_node.next = current.next
        current.next = new_node

    # Find and print the middle node
    def find_middle(self):
        if self.head is None:
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def sum_pairs(self):
        current = self.head

        while current and current.next:
            print(current.data + current.next.data)
            current = current.next


def solution():
    ll = SinglyLinkedList()

    ll.append(8)
    ll.append(5)
    ll.append(3)

    ll.display()
    ll.find_middle()

    ll.reverse()
    ll.display()

    ll.sum_pairs()


solution()
