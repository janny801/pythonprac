#return true if valid anagram 


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case; if not same char length 
        if len(s) != len(t): 
            #no possibility of anagram 
            return False

        seen = {} #(value, frequency) 
        #add to seen hashmap based on string 's' 
        for char in s: 
            if char in seen: 
                seen[char]+=1
            else: 
                seen[char] =1
        #remove from seen using string 't' 
        for char in t: 
            if char not in seen: 
                #no possibility for anagram 
                return False
            else: 
                #decrement
                seen[char]-=1
            #case; frequency drops below 0 
            if seen[char]<0: 
                return False
        
        #return true if made it this far lol 
        return True
        