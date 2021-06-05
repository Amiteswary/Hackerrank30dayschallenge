# Enter your code here. Read input from STDIN. Print output to STDOUT
def str_fun(s_list,t):
    for i in range(0,t):
        s1=""
        s2=""
        temp=s_list[i]
        n=len(s_list[i])
        if(temp[i]==0):
            s1=s1+temp[i]
        else:
            s2=s2+temp[i]
            


t=int(input())
s_list=[]
for i in range(0,t):
    s=str(input())
    s_list.append(s)
str_fun(s_list,t)
