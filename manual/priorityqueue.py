#practice making a priority queue using a minheap 
#no 'import heapq' 

class priorityqueue: 
    def __init__(self):  
        self.heap=[]
    
    def push(self, item): 
        #add item to the end of the list first then do the reordering
            #this preserves complete binary tree structure 
            #heap shape is correct, but minheap ordering might be incorrect
        self.heap.append(item) 







