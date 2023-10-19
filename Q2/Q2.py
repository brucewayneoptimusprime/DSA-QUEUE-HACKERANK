from queue import LifoQueue
import fileinput

class Queue_ts():
    def __init__(self):
        self.stack1 = LifoQueue()
        self.stack2 = LifoQueue()

    def change_stack(self, st_from, st_to):
        while not st_from.empty():
            st_to.put(st_from.get())
    
    def enqueue(self, el: int):
        self.stack2.put(el)
    
    def dequeue(self,):
        if self.stack1.empty():
            self.change_stack(self.stack2, self.stack1)
        return self.stack1.get()
        
    def print_front(self,):
        el = self.dequeue()
        print(el)
        self.stack1.put(el)

if __name__ == '__main__':
    num_queries = None
    queue = Queue_ts()
        
    for line in fileinput.input():
        if not num_queries:
            num_queries = int(line.rstrip())
            continue
        
        query = line.rstrip().split()        
        if query[0]=='1':
            queue.enqueue(int(query[1]))
        elif query[0]=='2':
            queue.dequeue()
        else:
            queue.print_front()
