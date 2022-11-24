import CFG
import CYK
import lexer

grammar = CFG.Grammar().parseCFG('grammar.txt')

# for x in grammar:
#     print(x)

# lexer = ['a', 'a', 'b', 'b', 'a', 'b']
# ans = CYK.cykParse(lexer, grammar)

lexer = lexer.parseToToken('test/tc3.js')
# lexer = list(filter(lambda a: a != 'newline', lexer))
print(lexer)
ans = CYK.cykParse(lexer, grammar)

print(ans)
