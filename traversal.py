class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None

    def traverse(self, stop_val):
        current = self.head 
        while current != None:
            print (current.data)
            if current.data == stop_val:
                break
            current = current.next
        if current == None:
            print("Value not found")


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

ll = SinglyLL()
ll.head = node1
ll.traverse(30)

