"# GraphTheory" 
G00344474@gmit.ie

This is my project for Graph Theory.
This project entails writing a program in python to execute expressions of strings using Thompson's Algorithm.
This program must build a non-deterministic finite automata from the regular expression, using the three (or more) Characters, some with special meaning. | * , which mean concatenate, or and Kleene star

Running:
Parse the regular expressions from Infix notation to Postfix notataion, using the shunting algorithm.
Initialise the special characters to be used with there precedence over each other.
Loop through the strings 1 character at a time, if you come across an opening bracket, push it to the stack, if closing bracket pop it to the output until opening bracket again.
If character is an operator, push to stack after popping lower or equal precedence operators from top of stack to output. Regular characters will be instantly pushed to the output, then push all remaining operators from the stack to the output. And return your postfix regex.

Using Thompson's algorithm, represent a state with 2 arrows, labelled by label and use None for a label representing 'e' arrows
We represent an nfa by its initial and accept states. The compile definition compiles a postfix regular expression into an nfa. Once in the compile def, if the operator is "." we pop 2 nfa's off the stack, connect the first nfa's accept state to the second's initial, and then push the nfa to the stack
If the operator is "|" we pop the 2 nfa's off the stack, create a new accept state connecting the accept of the 2 nfa's popped from the stack to the new stack and then push the new nfa to the stack.
If the operator is "*" we pop a single nfa from the stack, create a new initial and accept states, Join the new initial state to nfa1's initial state and the new accept state. Join the old accept state to the new accept state and nfa1's initial state. Push the new nfa to the stack, 
If the operator is "+" we pop 2 nfa's off the stack, connect the first nfa's accept state to the second's initial, and then push the nfa to the stack
if the operator is "?" we pop 2 nfa's off the stack, join the first nfa's accept state to the second's initial, and then push the nfa to the stack
Otherwise we create a new initial and accept states, join the initial state to the accept state using an arrow labelled C and push the new NFA to the stack.
We return the new NFA (newnfa) which should only have a single nfa on it at this point.

In the definition for the followes, we return a set of states that can be reached from the state floowing e arrows,
We create a new set as state as its only member. We check if the state has arrows labelled 'e' from them. Check if edge1 is a state (if theres an edge, follow it). Check if edge2 is a state(if theres an edge, follow that one). Then return the set of states.

In the definition for match this compiles the infix notation to postfix and creates an nfa from it. We then shunt and compile the regular expressions. Add the current set of state, and the next set of state, and add the initial state to the current set.
Loop through each character in the strings, and loop through the current set of states. Check if the current set labelled s and add edge1 state to the next set including all the states from the "e" arrows. Once done, set current to next and clear next.
Then check if the accept state is in the list of the current state



Research

Videos, and resources from Ian on LearnOnline.

Regular Expression to NFA
https://www.youtube.com/watch?v=RYNN-tb9WxI

A* Algorithm
https://www.youtube.com/watch?v=ob4faIum4kQ

Thompsons Algorithm
http://www.cs.may.ie/staff/jpower/Courses/Previous/parsing/node5.html

https://en.wikipedia.org/wiki/Thompson%27s_construction

https://stackoverflow.com/questions/17983289/how-can-i-convert-a-regex-to-an-nfa

https://gist.github.com/taylor/1452682

https://xysun.github.io/posts/regex-parsing-thompsons-algorithm.html
