# input is all lowercase 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #map to count list of anagrams 
        groups = {}

        for word in strs: 
            #create frequency array for 26 lowercase chars 
            count = [0] * 26
            for char in word: 
                index = ord(char) - ord('a') #convert character into a number between 0 - 25
                count[index]+=1
            
            # print("word: ", word, "- count : " , count) 
            #convert to tuple 
            key = tuple(count) 
            print("key: ", key) 
            #add word to the correct anagram group 
            if key in groups: 
                groups[key].append(word) 
            else: 
                groups[key] = [word]
        #return grouped anagrams 
        return list(groups.values())

