class StackQueue:
    # We use lists but limit ourselves to 
    # pop, append, and [-1] (e.g. peek) operations
    # to emulate a stack.
    stack1 = []
    stack2 = []
    
    def enqueue(self, value):
        self.stack1.append(value)
    
    def dequeue(self):
        if len(self.stack2):
            return self.stack2.pop()
            
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()
        
    def peek(self):
        if len(self.stack2):
            return self.stack2[-1]
            
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
        return self.stack2[-1]
    

if __name__ == "__main__":
    q = int(input())
    inputs = []
    for i in range(q):
        inputs.append(tuple(map(int, input().split())))
    
    queue = StackQueue()
    for t in inputs:
        if t[0] == 1:
            queue.enqueue(t[1])
        elif t[0] == 2:
            queue.dequeue()
        elif t[0] == 3:
            print(queue.peek())