# given 
# - input; size of the rangoli 

# output
# - the rangoli dawg 


def print_rangoli(size):
    # your code goes here

    #find  ith letter of alphabet (i= size) 
    ithLetter = chr(ord('a') + size-1) 
    
    charLength = (size*3) + (size-3) #char length for each row
    amtofrows = size + (size-1) #amt of rows in output

    
    for row in range(amtofrows): 
        # #test ; print one new additional letter each row 
        # letter = chr(ord('a')+ row)
        # print(letter)
        
        #calculate how many letters in that row 
        if row<size: 
            amtLetters = (row*2) +1
            print(amtLetters)
            #above; allows us to build top half 
            #then js flip on other side 
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)