#Singly Linked List
#Time Complexity = O(n)
#Space Complexity = O(n)

class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        newNode=ListNode(data)
        if self.head = None:
            self.head=newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode
        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        n=self.head
        foundNode=None
        while n.next is not None:
            if(key==n.data):
                print("found a match", n.data)
                foundNode=n
            n=n.next
        
        if(foundNode is None):
            print("Did not find key")

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        if self.head == None:
            print("Empty linkedlist!")
            return 

        if self.head.data==key:
            self.head=self.head.next
            return

        n=self.head
        while n.next:
            if(n.next.data==key):
                n.next=n.next.next
                return
            n=n.next
    def show(self):
        if self.head==None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next

ll=SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print(ll.show())

ll.find(30)

ll.remove(20)

print("\nAfter Removing:")
ll.show()



