# nfa = {'A' : {'a':['A','B'], 'b':['A']}, 'B' : {'a':['C'], 'b':['C']}, 'C' : {'a':['D'], 'b':['D']},'D' : {'a':[], 'b':[]},}
# n = 4
# t = 2

# nfa  = {'A': {'0': ['A'], '1': ['A', 'B']}, 'B': {'0': ['C'], '1': ['C']}, 'C': {'0': [], '1': []}}
# n = 3
# t = 2

def print_table(d,isNFA=0):
    states =list(d.keys())
    path = list(d[states[0]].keys())
    max_len = 9
    
    print(" "*(max_len),end="")
    for i in range(len(path)):
        print(path[i],end=" "*(max_len-len(path[i])))
    print()

    for i in range(len(states)):
        print(states[i],end=" "*(max_len-len(states[i])))
        for j in range(len(path)):
            if(isNFA):
                print(", ".join(d[states[i]][path[j]]),end=" "*(max_len-len(d[states[i]][path[j]])*3+2))
            else:
                print(d[states[i]][path[j]],end=" "*(max_len-len(d[states[i]][path[j]])))
        print()

nfa = {}
n = int(input("No. of states : "))
t = int(input("No. of transitions : "))
for i in range(n):
    state = input("state name : ")
    nfa[state] = {}
    for j in range(t):
        path = input("path : ")
        print("Enter end state from state {} travelling through path {} : ".format(state, path))
        reaching_state = [x for x in input().split()]
        nfa[state][path] = reaching_state

print("\nNFA :- \n")
print(nfa)
print("\nPrinting NFA table :- ")
print_table(nfa,1)

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]

new_states_list = []

#-------------------------------------------------

dfa = {}
keys_list = list(list(nfa.keys())[0])
path_list = list(nfa[keys_list[0]].keys())
print(keys_list)
print(path_list)

dfa[keys_list[0]] = {}
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])
    dfa[keys_list[0]][path_list[y]] = var
    if var not in keys_list:
        new_states_list.append(var)
        keys_list.append(var)

while len(new_states_list) != 0:
    dfa[new_states_list[0]] = {}
    for i in range(len(path_list)):
        temp = []
        for j in range(len(new_states_list[0])):
            temp += nfa[new_states_list[0][j]][path_list[i]]
        s = ""
        s = s.join(temp)
        if s not in keys_list:
            new_states_list.append(s)
            keys_list.append(s)
        dfa[new_states_list[0]][path_list[i]] = s

    new_states_list.remove(new_states_list[0])

print("\nDFA :- \n")
print(dfa)
print("\nPrinting DFA table :- ")
print_table(dfa)

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nFinal states of the DFA are : ", dfa_final_states)