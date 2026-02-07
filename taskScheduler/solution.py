#goal; return min number of cpu cycles to complete all tasks 

import heapq#will be implemented as a max heap in the code 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #count task frequencies
        counts = {} 
        #key; task 
        #value; frequency the same tasks appears in the given input array 
        for task in tasks: 
            if task in counts: 
                counts[task] +=1
            else: 
                counts[task]=1
        
        #build a max heap by inserting negative values 
        heap = []
        for task in counts: 
            heapq.heappush(heap, -counts[task])
        
        #cooldown list (remaining_count, available_time)
        cooldown=[]
        #stores tasks that were just executed 
        #cannot be run again b/c of cooldown rule (separated by n cpu cycles)
        time = 0

        #simulate the cpu cycles
            #keep looping while either heap or cooldown is not empty 
        while heap or cooldown: 
            time +=1

            #run a task if possible 
            if heap: 
                count = heapq.heappop(heap)
                count +=1 #decrease remaining count (since we push negative values) 
                if count != 0: 
                    #put task into cooldown for 'n' amount of time (problem constraint) 
                    cooldown.append((count, time+n))
            #check cooldown list for tasks that are ready 
            i = 0
            while i<len(cooldown): 
                if cooldown[i][1] == time: 
                    heapq.heappush(heap, cooldown[i][0])
                    cooldown.pop(i)
                else: 
                    i +=1
        return time






