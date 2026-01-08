if __name__ == '__main__':
    students=[] #list stores [name,score]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    #list that stores only the scores 
    scores=[]
    
    #get each score from the students list 
    for student in students: 
        scores.append(student[1])
        
    #lowest score in scores list 
    lowest = min(scores) 
    
    #set 2nd lowest to large value 
    secondlowest = float('inf')
    
    #find the 2nd lowest value 
    for s in scores:
        #if not same as lowest and smaller then secondlowest 
        if s!= lowest and score< secondlowest: 
            secondlowest=s
    
    names = [] #used to return ppl with second lowest score
    #find matching names with second lowest score 
    for student in students: 
        if student[1]== secondlowest: 
            names.append(student[0])
    names.sort() #sort alphabetically 
    
    for name in names: 
        print(name) 