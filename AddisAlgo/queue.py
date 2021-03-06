'''
Implementation of Queue for AdisAlgo 
The class consists of 
                    - Enqueue
                    - Dequeue
'''

class queueClass:
    def __init__(self, size):
        self.size = size
        self.source = [0 for i in range(self.size)] 
        self.front = -1
        self.rear = -1

    # Check if the queue is empty  
    def isEmpty(self):
        return True if self.front == -1 else  False 
    # Check if the queue is full 
    def isFull(self):
        return True if ((self.front - self.rear > 0) or (self.rear - self.front == len(self.source) -1)) else  False 

    # Dequeue from a queue
    def dequeue(self):
        
        if self.isEmpty() != True:
            if self.front == self.size -1:
                self.front = -1
            self.front += 1
            return self.source[self.front - 1]
        else:
            print("The Queue is empty, No more vlaues to dequeue", "\n")
            return None
        
    # Enqueue an element to the queue
    def enqueue(self, value):
        
        if self.isFull() != True:
            if self.rear == self.size -1:
                self.rear = -1
            if self.isEmpty() == True:
                self.front += 1
            self.rear += 1
            self.source[self.rear] = value
            return True
        else:
            print("The Queue is full, cannot enqueue anymore values", "\n")
            return None

    