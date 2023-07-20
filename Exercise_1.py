#Stack using array

#Time Complexity = O(1)
#Space Complexity = O(1)

class myStack:
     def __init__(self):
     	self.Stack=[]

     def isEmpty(self):
     	if len(self.Stack)<=0:
     		return True
     	else:
     		return False

     def push(self, item):
     	if(!self.isEmpty()):
     		print("Stack is full")
     		return 
     	self.Stack.append(item)
         
     def pop(self):
        if(self.isEmpty()):
        	print("Stack is empty")
        else:
        	item=self.Stack[-1]
        	del self.Stack[-1]      #del top element of the stack
        	return item
        
     def peek(self):
     	if(self.isEmpty()):
     		print("Stack is empty")
     		return
     	else:
     		return self.Stack[-1]  #top element of the stack
        
     def size(self):
     	return len(self.Stack)
         
     def show(self):
     	return self.Stack
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
