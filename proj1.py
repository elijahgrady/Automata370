import sys

def main(argv):
    # takes input from the command line specified file and initialize into local variables
    with open(sys.argv[1], "r") as x:
        #stores number of states
        numStates = int(x.readline().rstrip('\n'))
        #stores the alphabet, as a list
        alphabet = list(x.readline().rstrip('\n'))

        #Reads in a list of state transitions, with each transition a list of size 3
        stateTransitions = []
        line = x.readline().rstrip('\n')

        while(line.__len__() != 1):
            splitted = line.split('\'')
            hold = []
            for i in splitted:
                hold.append(i.replace(' ',''))
            stateTransitions.append(hold)
            line = x.readline().rstrip('\n')

        #Reads in the start state
        startState = int(line)

        #Reads in the accept states, as a list
        acceptStates = x.readline().rstrip('\n').split(' ')
        for a in acceptStates:
            try:
                a= int(a)
            except:
                acceptStates.remove(a)

        #Reads in input strings
        inputStrings = []
        for line in x:
            line = line.rstrip('\n')
            inputStrings.append(line)

        #Creates the DFA, and runs the computation on each input string
        myDFA = DFA(alphabet,numStates,acceptStates,stateTransitions,startState)
        for x in inputStrings:
            myDFA.inputstring(x)

'''
This is a class that represents a DFA.
Each DFA object has an alphabet stored as a list of symbols, a list of states, and a current state
'''
class DFA:
    '''
    Constructs a DFA object
    @:param E, a list of symbols in the alphabet
    @:param Q, the number of states
    @:param F, a list of accepting states
    @:param transitions, the list of transitions
    @:param q0, the start state
    '''
    def __init__(self, E, Q, F, transitions, q0):
        self.alphabet = E
        self.states = {}
        self.currentstate = q0

        #Constructs State object 1 : Q
        for x in range(1,Q+1):
            self.states[x] = State(x, F, transitions)

    '''
    Performs a computation on the input string
    @:param inputstring, the string the computation is performed on
    @:return Prints out Accept or Reject, based on the outcome of the computation
    '''
    def inputstring(self, inputstring):
        original = self.currentstate
        for x in list(inputstring):
            self.currentstate = int(self.states[self.currentstate].transitions[x])
        if self.states[self.currentstate].accept is True:
            print("Accepts")
        else:
            print("Rejects")
        self.currentstate = original

'''
A class that represents a State object
Each State object has a state number, an accept flag, and a dictionary of transitions
'''
class State:
    '''
    Constructs a State object
    @:param state, the state number
    @:param accepts, a list of accept states
    @:param transitions, a list of transitions for the DFA
    '''
    def __init__(self, state, accepts, transitions):
        self.statenum = int(state)
        self.accept = False
        for x in accepts:
            if int(x) is int(state):
                self.accept = True
        self.transitions = {}
        for x in transitions:
            if int(x[0]) is int(state):
                self.transitions[x[1]] = x[2]

if __name__ == "__main__":
    main(sys.argv[1])

