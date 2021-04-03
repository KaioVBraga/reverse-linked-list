def showLinkedList(head):
    current = head
    print(current.value)

    while(current.next != None):
        current = current.next
        print(current.value)

def reverseLinkedList(head):
    current = head
    
    nextNode = current.next
    current.next = None

    while(nextNode != None):
        nextNextNode = nextNode.next
        nextNode.next = current

        current = nextNode
        nextNode = nextNextNode

    return current

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = LinkedList(10)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)
node6 = LinkedList(215)
node7 = LinkedList(53)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

showLinkedList(node1)
print()
node = reverseLinkedList(node1)
showLinkedList(node)