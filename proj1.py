import sys, getopt, DFA, tokenize


# ALL WE NEED TO DO IS GET OUR INPUT TO BE IN THE SAME FORMAT AS THE 'CHEATING' INPUT

def main(argv):
    # takes input from the command line specified file and initialize into local variables
    with open(sys.argv[1], "r") as x:


        numstates = x.readline().rstrip('\n')
        print(numstates)

        alphabet = x.readline().rstrip('\n')
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




if __name__ == "__main__":
    main(sys.argv[1])

