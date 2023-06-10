file = open("program.c",'r')

spl_symbol=["[","]","(",")","{","}",";",":"]
keywords=["auto","break","case","char","const","continue","default",
"do","double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while"]
number=['1','2','3','4','5','6','7','8','9','0']
arith_op = ['+','-','*','/','%']
relat_op = ['==','!=','>=',"<=",'<','>']
logic_op = ['&&','||','!']
bitwise_op = ['&','|','^','<<','>>']
assign_op = ['=','+=','-=','*=','/=','%=']

line = file.readlines()
l=[x.replace('\n','').strip() for x in line]

nkey=set()
nnum = set()
nop = set()
nsym = set()
nide = set()
pre=0

print("\nLexical analysis\n")

i=0
while i<(len(l)):
    if '#' in l[i]:
        print(l[i],"is a preprocessor directive")
        pre+=1
    else:
        code = l[i].split()
        for j in range(len(code)):
            if code[j] == "\\\\":
                str=" ".join(code[j:])
                print("\n",str,"is a single line comment")
                break
            elif code[j] == "/*":
                str=" ".join(code[j:])
                i+=1
                code = l[i].split()
                while "*/" not in code:
                    str+="\n"
                    str+=" ".join(code[:])
                    i+=1
                    code = l[i].split()
                str+="\n"
                str+=" ".join(code[:])
                print("\n",str,"is a multi line comment\n")
                break
            elif code[j] in keywords:
                print(code[j],"is a keyword")
                nkey.add(code[j])
            elif code[j] in number:
                print(code[j],"is a number")
                nnum.add(code[j])
            elif code[j] in spl_symbol:
                print(code[j],"is a separator")
                nsym.add(code[j])
            elif code[j] in arith_op:
                print(code[j],"is a arithmetic operator")
                nop.add(code[j])
            elif code[j] in relat_op:
                print(code[j],"is a relational operator")
                nop.add(code[j])
            elif code[j] in logic_op:
                print(code[j],"is a logical operator")
                nop.add(code[j])
            elif code[j] in bitwise_op:
                print(code[j],"is a bitwisse operator")
                nop.add(code[j])
            elif code[j] in relat_op:
                print(code[j],"is a relational operator")
                nop.add(code[j])
            elif code[j] in assign_op:
                print(code[j],"is a assignment operator")
                nop.add(code[j])
            else:
                print(code[j],"is a identifier")
                nide.add(code[j])
    i+=1

file.close()

print()
print("Total no. of keywords =",len(nkey))        
print("Total no. of constants =",len(nnum))                                        
print("Total no. of operators =",len(nop))                                                                        
print("Total no. of identifiers =",len(nide))                                        
print("Total no. of symbols =",len(nsym))                                        
print("Total no. of tokens =",len(nkey)+len(nnum)+len(nop)+len(nide)+len(nsym)+pre)                                        