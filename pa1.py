#!/usr/bin/python

import sys, getopt, DFA

def main(argv):

    #takes input from the command line specified file and initialize into local variables
    fileIN = open(sys.argv[1], "r")
    line = fileIN.readline()
    NUM_STATES = line
    print(NUM_STATES)
    line = fileIN.readline()
    ALPHA_BET = list(line)
    print(ALPHA_BET)
    line = fileIN.readline()
    TRANS_LIST = []
    while(list(line).__len__()==8):
        TRANS_LIST.append(list(line))
        line = fileIN.readline()
    print(TRANS_LIST)
    TRANS_DICT = {}
    #CONVERT THE LIST OF TRANSITIONS INTO A TRANSITION FUNCTION DICTIONARY
    START_STATE = line
    print(START_STATE)
    line = fileIN.readline()
    ACCEPT_STATES = list(line)
    print(ACCEPT_STATES)
    INPUT_STRINGS = []
    line = fileIN.readline()
    while(line.__len__()>0):
        INPUT_STRINGS.append(line)
        line = fileIN.readline()
    print(INPUT_STRINGS)
    this_dfa = DFA.DFA(NUM_STATES, ALPHA_BET, TRANS_DICT, START_STATE, ACCEPT_STATES)
    this_dfa.run_with_input_list(INPUT_STRINGS)

if __name__ == "__main__":
   main(sys.argv[1])

