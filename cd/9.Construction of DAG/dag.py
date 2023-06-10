print("Enter the expressions with () brackets : ")
e = input()

# e="(((a+b)*c)-((a+b)*c))"

track=0
i=0
j=0
dag=[]
dict={}
while e[0]=="(":
    while e[i]!=")":
        i+=1
    j=i
    while e[j]!="(":
        j-=1
    
    input=e[j:i+1]

    for k in range(1,len(input)-1):
        if input[k].isalpha() and input[k] not in dict:
            l=0
            r=0
            ptr=track
            track+=1
            label=input[k]
            dict[input[k]]=ptr
            dag.append([ptr,l,r,label])
        elif input[k].isdigit():
            pass
        elif input[k] in ['+', '-', '*', '/']:
            index=k
    label=input[index]
    if input[index-1]!="(":
        l=dict[input[index-1]]
    else:
        l=0
    
    r=dict[input[index+1]]
    ptr=track
    track+=1
    dag.append([ptr,l,r,label])
    dict[str(ptr)]=ptr
    e=e.replace(input,str(ptr))
    i=0
    
print("\nDAG : \n")
print("PTR \tLEFT \tRIGHT \tLABEL")
for x in dag:
    for y in x:
        print(y,end="   \t")
    print()
        


