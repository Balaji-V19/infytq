#PF-Assgn-41
ls=[]
def find_ten_substring(num_str):
    le=len(num_str)
    va='0'
    for i in range(le):
        if(int(va)+int(num_str[i])<=10):
            va=va+num_str[i]
        else:
            ls.append(va+num_str[i])
            if(le>0):
                return find_ten_substring(num_str[1:len(num_str)])
            else:
                break
       
    print(ls)
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
