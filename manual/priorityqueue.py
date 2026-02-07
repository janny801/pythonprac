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

        #start "bubble up" step from index of new item 
            #new item always added at the last index 
            #ie swap upwards until it is larger then its parent
        i = len(self.heap)-1

        while i> 0: 
            #compute the parent index using heap index math 
            parent = (i-1)//2 #works for both left and right children since using 
                                #floor division 
            
            if self.heap[i][0] < self.heap[parent][0]: 
                #if parent is larger value 
                    #then swap child with its parent 
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

                #update 'i' so we can continue bubbling up 
                i = parent 
            else: 
                #if parent is already smaller or equal 
                #min heap property is satisfied 
                break
    

    def pop(self): 
        #goal; remove and return the highest priority item 
            #smaller number == higher priority
            #highest priority item is always at the root 
        #check if heap is empty 
        if not self.heap: 
            return None #if empty --> nothing to return 

        if len(self.heap)==1: 
            return self.heap.pop()

        #save the root item 
        top = self.heap[0]
        self.heap[0] = self.heap.pop() #remove last element and move it to the root 

        i =0 #bubble down starting at the root index 

        #keep bubbling down until ... 
            #value is swapped to the correct spot or 
            # value is smaller then both children 
        while True: 
            #compute indices of left and right children 
            left = 2*i + 1
            right = 2*i +2

            #assume current node is the smallest for now (will be compared to its children and updated) 
            smallest = i 

            #if left child is smaller then the current smallest update 
            if left< len(self.heap) and self.heap[left][0] < self.heap[smallest][0]: 
                smallest = left
            #if right child is smaller then current smallest update 
            if right<len(self.heap) and self.heap[right][0] < self.heap[smallest][0]: 
                smallest = right
            
            #if smallest is not 'i' --> one of the children are smaller and swap is needed
            if smallest !=i: 
                #swap current node with smallest node 
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                #move 'i' down to where the item got swapped to 
                    #since still might be larger then its new children (continue bubbling down) 
                i = smallest 
            else: 
                #smallest ==i in this case; break 
                break
        return top #returns item that was originally at the root 

def main():
    # create the priority queue
    pq = priorityqueue()

    # initial tasks (priority, task_name)
    tasks = [
        (3, "do laundry"),
        (1, "finish homework"),
        (2, "buy groceries"),
        (0, "emergency task")
    ]

    print("ADDING TASKS\n")

    # add tasks one by one and print heap after each add
    for task in tasks:
        pq.push(task)
        print("added:", task)
        print("current heap:", pq.heap)
        print()

    print("REMOVING TASKS\n")

    # remove tasks one by one and print heap after each removal
    while pq.heap:
        removed = pq.pop()
        print("removed:", removed)
        print("current heap:", pq.heap)
        print()


if __name__ == "__main__":
    main()
        







