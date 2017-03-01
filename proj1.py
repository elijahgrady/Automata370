import sys

def main(argv):
    # takes input from the command line specified file and initialize into local variables
    with open(sys.argv[1], "r") as x:

        numStates = int(x.readline().rstrip('\n'))

        alphabet = list(x.readline().rstrip('\n'))

        stateTransitions = []

        line = x.readline().rstrip('\n')

        while(line.__len__() != 1):
            splitted = line.split('\'')
            hold = []
            for i in splitted:
                hold.append(i.replace(' ',''))
            stateTransitions.append(hold)
            line = x.readline().rstrip('\n')

        startState = int(line)

        acceptStates = x.readline().rstrip('\n').split(' ')
        for a in acceptStates:
            try:
                a= int(a)
            except:
                acceptStates.remove(a)

        inputStrings = []

        for line in x:
            line = line.rstrip('\n')
            inputStrings.append(line)

        myDFA = DFA(alphabet,numStates,acceptStates,stateTransitions,startState)
        for x in inputStrings:
            myDFA.inputstring(x)

class DFA:

    def __init__(self, E, Q, F, transitions, q0):
        self.alphabet = E
        self.states = {}
        self.currentstate = q0

        #Constructs State object 1 : Q
        for x in range(1,Q+1):
            self.states[x] = State(x, F, transitions)

    def inputstring(self, inputstring):
        original = self.currentstate
        for x in list(inputstring):
            self.currentstate = int(self.states[self.currentstate].transitions[x])
        if self.states[self.currentstate].accept is True:
            print("Accepts")
        else:
            print("Rejects")
        self.currentstate = original

class State:

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

