class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev  



linkedList = LinkedList()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

linkedList.head = n1
n1.next = n2
n2.next = n3

print("Linked List -> ")
linkedList.printLinkedList()

linkedList.reverse()

print("Reversed Linked List ->")
linkedList.printLinkedList()
