n = int(input("Enter the no. of variables : "))
dict = {}
flag = 0
for i in range(n):
    var = input(f"Enter the variable-{i+1} : ")
    type = input(f"Enter the type of the variable \t float-f \t int-i : ")
    dict[var] = type

expr = input("Enter the expression : ").split()
if '/' in expr:
    flag = 1

if dict[expr[0]]=='f':
    print("Data type correctly defined.!")
else:
    for i in range(2,len(expr)):
        if expr[i] not in ['+','-','*','/'] and dict[expr[i]]=='f':
            flag=1
            break
    if flag==1:
        print(f"{expr[0]} should be in float datatype.!")
    else:
        print("Data type correctly defined.!")
