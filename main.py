import TXTtoCFG
import CFGtoCNF

cfg = TXTtoCFG.parseCFG('testgrammar3.txt')

cfg = CFGtoCNF.CFG(cfg)
cfg.CFGtoCNF()
