#stack using linked list
#Time complexity = O(n)
#Space complexity = O(n) 

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head=None
        n=self.head
        
    def push(self, data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode

    def pop(self):
        popped=None
        if self.head is None:
            print("Stack is empty")
            return None
        else:
            n = self.head
            while n.next is not None:
                if n.next.next is None:
                    popped_val = n.next.data
                    n.next = None
                else: 
                    n = n.next
            return popped_val

a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
