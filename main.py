import CFG
import CYK

grammar = CFG.Grammar().parseCFG('test/testgrammar3.txt')

for x in grammar:
    print(x)

lexer = ['a', 'a', 'a', 'a']
ans = CYK.cykParse(lexer, grammar)

print(ans)
