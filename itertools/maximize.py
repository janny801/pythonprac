from itertools import product
# given 
# line 1;  2 integers
#     - k; amt of lines that will follow 
#     - m; modulus used in the final calculation 

# following lines; 
#     - first digit; amt of digits in that line 
#     - followed by rest of digits 
    
if __name__ == '__main__': 
    #main
    
    n= map(int, input().split())#holds 'k' and 'm' 
    #convert to list so can extract values 
    ls= list(n) 
    k= ls[0] #amt of lines that will follow
    modulus = ls[1] #used in final calculation
    
    
    arrays= [] #holds all the proper arrays 
    for i in range(k): 
        #get input lines and values 
            #first value is amt in line , following are actual values
        rawline= list(map(int, input().split())) #each working line gets its own list 
        
        #add to the 'arrays' list the line without the first element 
        temp =[] 
        for i in range(1, len(rawline)): 
            temp.append(rawline[i])
        arrays.append(temp)
    
    
    #find the max value of 's' 
    x= product(*arrays) #ie (array1, array2, array3)
    maxS = float('-inf')
    for i in x: 
        s=0
        for j in i: 
            s = s+ (j**2) #formula
        s= s%modulus
        if s> maxS: 
            maxS = s
    
    print(maxS)
            
            
        
    
