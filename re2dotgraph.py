#!/usr/bin/env python

import FSA as fsa
import reCompiler as recompiler
import os, sys

regex = None
dotstring = None
graphfile = "regex.png"

def getDotString():
    global regex, graphfile, dotstring

    print
    print "[+] Generating dot string ..."
    fsa4re = recompiler.compileRE(regex)
    fsa4re = fsa4re.sorted()
    fsa4re = fsa4re.determinized()
    fsa4re = fsa4re.minimized()
    fsa4re = fsa4re.trimmed()

    print "[+] Label: %s" % (fsa4re.label)
    print "[+] states: %s" % (fsa4re.states)
    print "[+] states count: %d" % (len(fsa4re.states))
    print "[+] initialState: %s" % (fsa4re.initialState)
    print "[+] finalStates: %s" % (fsa4re.finalStates)
    print "[+] alphabet: %s" % (fsa4re.alphabet)
    print "[+] transitions:"

    for transition in fsa4re.transitions:
        print "\t%s" % (str(transition))

    dotstring = fsa4re.toDotString()
    print

def genDotGraph():
    global regex, graphfile, dotstring

    print "[+] Generating dot graph ..."

    try:
        fo = open('regex.dot', 'w')
        fo.write(dotstring)
        fo.close()
        dotcli = "dot -Tpng regex.dot >%s" % (graphfile)
        os.system(dotcli)
    except Error, ex:
        print "[-] Something bad happened. Find out why (Don't bug me till then :)"
        sys.exit(1)

    print "[+] regex: \'%s\' -> %s" % (regex, graphfile)
    print

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: %s <regex> [file.png]")
        sys.exit(1)
    else:
        regex = sys.argv[1]
        if len(sys.argv) > 2:
            graphfile = sys.argv[2]

        getDotString()
        genDotGraph()

