class Grammar:
    def __init__(self):
        self.CFG = {}
        self.keys = list(self.CFG.keys())
        self.values = list(self.CFG.values())
        self.index = 0

    def updateKeyVal(self):
        self.keys = list(self.CFG.keys())
        self.values = list(self.CFG.values())

    def createProduction(self, key, value):
        if key not in self.keys:
            self.CFG.update({key: [value]})
            self.updateKeyVal()
        else:
            self.CFG[key].append(value)

    def newVar(self):
        newvar = 'VAR' + str(self.index)
        self.index += 1
        return newvar

    def CFGtoCNF(self):

        startSymbol = self.keys[0]

        # If start symbol S is at the RHS of any production in the grammar, create a new production as: S0 -> S
        startInRHS = False
        for value in self.values:
            for item in value:
                if startSymbol in item:
                    startInRHS = True
                    break

        if startInRHS:
            self.createProduction('S0', [startSymbol])

        # self.printCFG()
        # Eliminate unit production
        recheck = True
        while recheck:
            changed = False
            for rule in self.CFG:
                for unit in self.CFG[rule]:
                    if (len(unit) == 1):
                        if not unit[0].islower():
                            self.CFG[rule].remove(unit)

                            # for x in self.CFG[rule]:
                            #     print(x)

                            # print()
                            for item in self.CFG[unit[0]]:
                                # print(unit)
                                # print(item)
                                self.CFG[rule].append(item)
                            changed = True
                            self.updateKeyVal()
            recheck = changed

        # remove useless production
        for rule in list(self.CFG):
            useless = True
            for value in self.values:
                for item in value:
                    if rule in item or rule == 'S0':
                        useless = False
                        break
            if useless:
                # print(self.CFG[rule])
                del self.CFG[rule]
                self.updateKeyVal()

        # Eliminate RHS with more than two non-terminals.
        recheck = True
        while recheck:
            changed = False

            for key in self.keys:
                for value in self.CFG[key]:
                    if len(value) > 2:

                        newVar = self.newVar()
                        newVal = [value[0], value[1]]

                        self.createProduction(newVar, newVal)
                        del self.CFG[key][(self.CFG[key]).index(value)][0:2]

                        self.CFG[key][(self.CFG[key]).index(
                            value)].insert(0, newVar)

                        self.updateKeyVal()
                        changed = True

            recheck = changed

    def parseCFG(self, filename):
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

        self.CFG = CFG
        self.updateKeyVal()

        self.CFGtoCNF()

        return self.CFG
