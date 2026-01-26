class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap + bucket sort solution 

        #count frequency of each number
        count = {} #number -> frequency
        for num in nums: 
            if num in count: 
                count[num ]+=1
            else: 
                count[num ]=1
        # create buckets where index = frequency 
        #buckets[i] = list of numbers that appear i times 
        buckets=[] #list of lists 
        for i in range(len(nums)+1): 
            #create buckets for every possible frequency 
            buckets.append([]) 
        
        #fill the buckets that matches how often it appears  
        for num in count: 
            freq= count[num]
            buckets[freq].append(num) #put number into bucket that matches it frequency 
        
        #collect k most frequent elements
        result = []
        freq= len(buckets)-1
        while freq> 0: 
            for num in buckets[freq]: 
                result.append(num)
                if len(result)==k: 
                    return result
            freq-=1

            



