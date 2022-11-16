# PARSING FILE TXT TO CFG GRAMMAR

# parse textfile CFG into dictionary
def parseCFG(filename):
    file = open(filename, 'r')
    CFG = {}

    # read rules line by line
    rules = file.readline()

    while rules != "":
        # remove enter
        rules = rules.replace("\n", "")
        # split parent and child
        parent, child = rules.split(" -> ")

        # Create empty list if parent not in CFG
        if parent not in CFG:
            CFG[parent] = []

        CFG[parent].append(child.split(' '))

        rules = file.readline()

    file.close()
    return CFG
