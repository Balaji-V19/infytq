#PF-Assgn-41
ls=[]
def find_ten_substring(num_str):
    le=len(num_str)
    va=''
    for i in range(le):
        l=len(va)
        res=0
        for k in range(l):
            res+=int(va[k])
        if(res+int(num_str[i])<10):
            if(res==0):
                va=num_str[i]
            else:
                va=str(res)+num_str[i]
        else:
            ls.append(va+num_str[i])
            if(le>0):
                return find_ten_substring(num_str[1:len(num_str)])
            else:
                break
    return ls
    
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
