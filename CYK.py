# Reference : https://www.geeksforgeeks.org/cocke-younger-kasami-cyk-algorithm/

# CYK Algorithm
def cykParse(javascript, CNF):
    string = javascript.split("")
    length = len(string)

    # Initialize the table
    T = [[set([]) for j in range(length)] for i in range(length)]

    # Filling in the table
    for j in range(length):

        # Iterate over the rules
        for lhs, rule in CNF.items():
            for rhs in rule:

                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == string[j]:
                    T[j][j].add(lhs)

        for i in range(j, -1, -1):

            # Iterate over the range i to j + 1
            for k in range(i, j):

                # Iterate over the rules
                for lhs, rule in CNF.items():
                    for rhs in rule:

                        # If a terminal is found
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)

    # If word can be formed by rules
    # of given grammar
    return len(T[0][length-1]) != 0
