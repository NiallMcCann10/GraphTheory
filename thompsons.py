#Thompsons contruction
#Niall McCann

#Shunting yard

def shunt(infix):
    """The shunting yard algorithm for converting infix expressions to postfix"""

   #Special Characters to be used with the regular expressions and their precedence over each other
    specials = {'*': 50, '.': 40, '|': 30}
    #Will eventually be the output
    pofix = ""
    #Operator stack
    stack = ""

    #Loop through string, 1 Charachter at a time
    for c in infix:
        #If an open bracket, push it onto the stack
        if c == '(':
            stack = stack + c
        #If a closing bracket, pop to the output until open bracket
        elif c == ')':
            while stack[-1] != '(':
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack[:-1]
        #If operator, push to stack after popping lower or equal precedence operators from top of stack to output
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        #Regular chars are pushed right away to output
        else:
            pofix = pofix + c
    #pop all remaining operators from stack to output
    while stack:
        pofix, stack = pofix + stack[-1], stack[:-1]
    
    #Return Postfix regular expression
    return pofix

##print(shunt("(a.b)|(c*.d)"))

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

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(pofix):
    """Compiles a postfix regular expression into an nfa"""
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
            nfa2.accept.edge1 = accept
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

def followes(state):
    """Return the set of states that can be reached from state following e arrows"""
    #Create a new set as state as its only member
    states = set()
    states.add(state)

    #Check if the state has arrows labelled e from them
    if state.label is None:
        #Check if edge1 is a state
        if state.edge1 is not None:
            #If theres an edge1 - follow it
            states |= followes(state.edge1)
        #Check if edge 2 is a state
        if state.edge2 is not None:
            #If theres an eddge2 - follow it
            states |= followes(state.edge2)
    
    #Returns the set of states.
    return states

#Compiles the infix to postfix and creates an nfa from it
def match(infix, string):
    """Matches String to the infix regular expressions"""
    #shunt and compilethe regular expression
    postfix = shunt(infix)
    nfa = compile(postfix)


    #The current set of state, and next set of states
    current = set()
    next = set()

    #Add the initial state to the current set
    current |= followes(nfa.initial)

    #Loop through each char in the string
    for s in string:
        #loop through the current set of states 
        for c in current:
            #Check if that state is labelled s
            if c.label == s:
              #Add the edge1 state to the next set including all the states from e arrows
              next |= followes(c.edge1)
        #Set current to next and clear next
        current = next
        next = set()

    #Check if the accept state is in the list of the current states
    return(nfa.accept in current)

#Testings
infixes = ["a.b.c*","a.(b|d).c*","(a.(b|d))*","a.(b.b)*.c"]
strings = ["","abc","abbc","abcc","abad","abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)