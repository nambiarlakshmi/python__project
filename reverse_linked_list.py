class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next =Node(30)
head.next.next.next= Node(40)

prev = None
current = head

while current is not None:
    next_node = current.next
    current.next = prev
    prev = current 
    current = next_node

head = prev
current = head

while current is not None:
    print(current.data)
    current = current.next