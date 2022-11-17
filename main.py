import TXTtoCFG
import CFGtoCNF

cfg = TXTtoCFG.parseCFG('grammar.txt')

# for x in cfg:
# print(x, cfg[x])

cfg = CFGtoCNF.CFG(cfg)
cfg.CFGtoCNF()
