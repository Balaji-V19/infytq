#PF-Assgn-44

def find_duplicates(list_of_numbers):
    co=0
    res=[]
    le=len(list_of_numbers)
    for i in range(le):
        se=0
        co=list_of_numbers[i]
        for j in range(i,le):
            if(co==list_of_numbers[j]):
                se+=1
        if(se>1):
            res.append(co)
            
    return list(set(res))        
                
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
