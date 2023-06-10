print("Enter the intemediate code : ")
j=0
line = input().split()
l=[]
while line:
    if line[3]=='+':
        opr = "ADD"
    elif line[3]=='-':
        opr = "SUB"
    if line[3]=='*':
        opr = "MUL"
    if line[3]=='/':
        opr = "DIV"
    l.append("MOV "+line[2]+", R"+str(j))
    l.append(opr+" "+line[4]+", R"+str(j))
    l.append("MOV "+"R"+str(j)+", "+line[0])
    j+=1
    line = input().split()

for x in l:
    print(x)

