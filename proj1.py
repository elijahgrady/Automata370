import sys, getopt, DFA, tokenize


# ALL WE NEED TO DO IS GET OUR INPUT TO BE IN THE SAME FORMAT AS THE 'CHEATING' INPUT

def main(argv):
    # takes input from the command line specified file and initialize into local variables
    with open(sys.argv[1], "r") as x:

        numstates = x.readline().rstrip('\n')
        print(numstates)

        alphabet = list(x.readline().rstrip('\n'))

        print(alphabet)

        STATE_TRANSITIONS = []

        line = x.readline().rstrip('\n')
        while(line.__len__() != 1):
            splitted = line.split('\'')
            hold = []
            for i in splitted:
                hold.append(i.replace(' ',''))

            STATE_TRANSITIONS.append(hold)
            line = x.readline().rstrip('\n')

        for y in STATE_TRANSITIONS:
            print(y)

        startstate = line
        print(startstate)

        ACCEPT_STATES = x.readline().rstrip('\n').split(' ')
        print(ACCEPT_STATES)

        inputStrings = []

        for line in x:
            line = line.rstrip('\n')
            inputStrings.append(line)
        for k in inputStrings:
            print(k)


class DFA:
    def __init__(self, E, Q, F, transitions, q0):
        self.alphabet = E
        self.states = {}
        self.startstate = q0
        #Constructs State object 1 : Q
        for x in range(1,Q+1):
            self.states[x] = State(x, F, transitions)

class State:
    def __init__(self, state, accepts, transitions):
        self.statenum = state
        self.accept = False
        for x in accepts:
            if int(x) is int(state):
                self.accept = True
        self.transitions = {}
        for x in transitions:
            if int(transitions[0]) is int(x):
                self.transitions[transitions[1]]= transitions[2]



if __name__ == "__main__":
    main(sys.argv[1])

