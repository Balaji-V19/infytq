#PF-Assgn-38

def check_double(number):
    le=len(str(number))
    do=number*2
    les=len(str(do))
    lst=sorted(list(str(do)),reverse=True)
    lst2=sorted(list(str(number)),reverse=True)
    if(str(lst)==str(lst2)):
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))
