#PF-Assgn-39
#This verification is based on string match.     

#Global variables
menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,250,3]

def place_order(*item_tuple):
    lst=list(item_tuple)
    men=list(menu)
    le=len(lst)
    le2=len(men)
    unavail=[]
    for i in range(le2):
        for j in range(0,le,2):
            if(men[i]==lst[j]):
                if(check_quantity_available(i,j+1)):
                    unavail.append(lst[j])
                    print (lst[j]," is available")
                else:
                    unavail.append(lst[j])
                    print(lst[j], " stock is over")
                break    
    l=len(unavail)
    res=[]
    for i in range(0,le,2):
        res.append(lst[i])
    re=set(res)-set(unavail)
    for i in re:
        if(len(set(res)-set(unavail))>0):
            print(i, " is not available")
    
                
    
            
    
    #print("<item name>is not available")
    #print("<item name>stock is over")
    #print ("<item name>is available")
    
def check_quantity_available(index,quantity_requested):
    if(quantity_available[index]>=quantity_requested):
        quantity_available[index]=quantity_available[index] - quantity_requested
        return True
    else:
        return False

place_order("Veg Roll",2,"Noodles",2)
place_order("Soup",1,"Veg Roll", 2, "Fried Rice1",1)
