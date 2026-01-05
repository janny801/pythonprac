

from typing import List


#how many 1's appear in binary form for every number 0 -> n 
def countBits( n:int) -> List[int]: 
    #initialize values with 0 
    ans = [0] * (n+1)

    #iterate thu 
    #//2 divide by 2+ (%2) remainder 
        #for each value up to (and including) n 

    for curr in range(1, n+1):
        ans[curr] = ans[curr//2] + (curr%2)
    return ans

if __name__ == '__main__': 
    #main func 
    testinput1= 2
    testinput2 = 5

    print(f"{testinput1} --> {countBits(testinput1)}")
    print(f"{testinput2} --> {countBits(testinput2)}")

    

