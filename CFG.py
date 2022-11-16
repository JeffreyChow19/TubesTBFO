class CFG:
    def __init__(self, CFG):
        self.CFG = CFG
        self.keys = list(CFG.keys())
        self.values = list(CFG.values())

    

    def createProduction(self, key, value):
        if key not in self.keys:
            self.CFG.update({key: [[value]]})
        else:
            self.CFG[key].append([value])

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
            self.createProduction('S0', startSymbol)

        print(self.CFG)
