n = int(input("Enter no. of expressions: "))
ic = {}
for i in range(n):
    print("For expression",i+1,":" )
    l = input("Left : ")
    r = input("Right : ")
    ic[l]=r

# n=5
# ic = {"a":9,"b":"c + d","e":"c + d","f":"b + e","r":"f"}

print("Intermediate Code : ")
for x in ic.keys():
    print(x,"=",ic[x])


key = [x for x in ic.keys()]
value = [x for x in ic.values()]

op={}
for i in range(n):
    t = key[i]
    for j in range(i+1,n):
        if t in value[j]:
            op[key[i]]=value[i]
            break
op[key[n-1]]=value[n-1]

print("Dead Code Elimination : ")
for x in op.keys():
    print(x,"=",op[x])


key = [x for x in op.keys()]
value = [x for x in op.values()]

for i in range(len(key)):
    r = value[i]
    for j in range(i+1,len(key)):
        if r == value[j]:
            for k in range(j+1,len(key)):
                key[k]=key[k].replace(key[j],key[i])
                value[k]=value[k].replace(key[j],key[i])
            key[j]=key[i]

print("Common Subexpression Elimination : ")
for i in range(len(key)):
    print(key[i],"=",value[i])

index=[]

for i in range(len(key)):
    for j in range(i+1,len(key)):
        if key[i]==key[j] or value[i]==value[j]:
            index.append(j)

for x in reversed(index):
    key.pop(x)
    value.pop(x)

print("Optimized Code : ")
for i in range(len(key)):
    print(key[i],"=",value[i])

