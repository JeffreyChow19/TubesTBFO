import TXTtoCFG
import CFGtoCNF
import CFG
import CYK


# cfg = TXTtoCFG.parseCFG('testgrammar3.txt')

# cfg = CFGtoCNF.CFG(cfg)
# cfg.CFGtoCNF()

# CFG = CFG.CFG()
grammar = CFG.Grammar().parseCFG('testgrammar3.txt')

for x in grammar:
    print(x)

lexer = ['a', 'b']
CYK.cykParse(lexer, grammar)
