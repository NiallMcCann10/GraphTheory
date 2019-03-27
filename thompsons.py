#Thompsons contruction
#Niall McCann

#Represents a state with 2 arrows, labelled by label
#Use None for a label representing 'e' arrows
class state:
    label = None
    edge1 = None
    edge2 = None

#An nfa is represented by its initial and accept states
class nfa:
    initial = None
    accept = None

    def _init_(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    nfastack = []

    for c in pofix:
        if c == '.':
            #Pop 2 nfa's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #connect  first nfa's accept state to the second's inital
            nfa1.accept.edge1 = nfa2.initial
            #Push nfa to the stack
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)

        elif c == '|':
            #Pop 2 nfa's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #Create a new initial state, connect it to initial states of nfa1 and nfa2 popped off the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            #create a new accept state connecting the accept states of the 2 nfa's popped from the stack to the new stack
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            #Push new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

        elif c == '*':
            #Pop a single nfa from the stack
            nfa1 = nfastack.pop()
            #Create a new initial and accept states
            initial = state()
            accept = state()
            #Join the new initial state to nfa1s initial state and the neew accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            #Join the old accept state to the new accept state and nfa1's initial state.
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #Push the new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

        else:
            #Create new initial and accept states
            accept = state()
            initial = state()
            #Join the initial state to the accept state using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            #Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)

    #nfastack should only have a single nfa on it at this point
    return nfastack.pop()

print(compile("ab.cd.|"))
print(compile("aa.*"))