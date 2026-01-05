class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array then use the two pointer method 

        nums.sort() 

        result = [] #this will be returned 
        n = len(nums) 

        for i in range(n): 
            #skip duplicate numbers 
            if i> 0 and nums[i] == nums[i-1]: 
                continue
            
            #set up the two pointers for indicies to go thru array 
            left = i+1 
            right = n-1

            #two pointer search 
            while left < right: 
                total = nums[i] +nums[left] +nums[right]

                if total ==0: 
                    #valid triplet found 
                    result.append([nums[i], nums[left], nums[right]])

                    #move left and right pointers past duplicates 
                    left +=1
                    right -=1

                    while left<right and nums[left] == nums[left-1]: 
                        #if same as prev value left pointer was poitning to
                        left +=1
                    
                    while left<right and nums[right] ==nums[right+1]: 
                        #if same as prev value right pointer was pointing to
                        right -=1
                elif total > 0: 
                    #total is too large 
                    right -=1
                else: 
                    left +=1
        return result 
                    
                

        