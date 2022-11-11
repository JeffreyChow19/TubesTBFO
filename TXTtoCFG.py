# PARSING FILE TXT TO CFG GRAMMAR

def parseCFG(filename):
    file = open(filename, 'r')
    CFG = {}

    # read rules line by line
    rules = file.readline()

    while rules != "":
        rules = rules.split(' -> ')
        rules = rules.remove('\n')
        parent, child = rules

        # Create empty list if parent not in CFG
        if parent not in CFG:
            CFG[parent] = []

        CFG[parent].append(child.split(' '))

        rules = file.readline()

    file.close()
    return CFG
