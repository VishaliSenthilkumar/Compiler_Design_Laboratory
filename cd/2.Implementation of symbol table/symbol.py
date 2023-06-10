import sys
file = open("program.c",'r')
l = file.readlines()

def isFunction(a):
    if '(' in a and ')' in a:
        return True
    return False

spl_symbol=["[","]","(",")","{","}",";",":","#"]
keywords=["auto","break","case","char","const","continue","default",
"do","double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while"]
number=['1','2','3','4','5','6','7','8','9','10']
operators = ['=','+','-','*','/','%']

print("\nSymbol Table\n")
print("Symbol \t addr \t\t\t type \t\t\t   size \tLine of declaration \t isFunction")

i=0
while i<len(l):
    code = l[i].split()
    for j in code:
        if j in keywords:
            location = id(j)
            print("\n{} \t {} \t\t keyword \t\t {}bytes \t {}\t\t\t {}\n".format(j, location,sys.getsizeof(j),i,isFunction(j)))
        elif j in number:
            location = id(j)
            print("\n{} \t {} \t constant \t\t {}bytes \t {}\t\t\t {}\n".format(j, location,sys.getsizeof(j),i,isFunction(j)))
        elif j in spl_symbol:
            location = id(j)
            print("\n{} \t {} \t special character \t {}bytes \t {}\t\t\t {}\n".format(j, location,sys.getsizeof(j),i,isFunction(j)))
        elif j in operators:
            location = id(j)
            print("\n{} \t {} \t operator \t\t {}bytes \t {}\t\t\t {}\n".format(j, location,sys.getsizeof(j),i,isFunction(j)))
        else:
            location = id(j)
            print("\n{} \t {} \t\t identifier \t\t {}bytes \t {}\t\t\t {}\n".format(j, location,sys.getsizeof(j),i,isFunction(j)))
        i+=1

file.close()
                                                  