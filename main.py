import CFG
import CYK
import lexer
import argparse
import time
from colorama import Fore, Style


def splash():
    print(Fore.YELLOW)
    print("============================")
    print("  JAVASCRIPT SYNTAX LINTER")
    print("        三位棉兰男神        ")
    print("============================")
    print(Style.RESET_ALL)


# argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
filename = args.file.name

# splash
splash()
print(Fore.BLUE +
      f'Checking {filename}...\nPlease wait for a moment...' + Style.RESET_ALL)

# timer start
start = time.time()

# grammar
grammar = CFG.Grammar().parseCFG('grammar.txt')

# lexer
lexer = lexer.parseToToken(filename)

# CYK algorithm
result = CYK.cykParse(lexer, grammar)

# time end
end = time.time()

# Result
if result:
    print(Fore.GREEN)
    print("|--------------------|")
    print("| Compile Success!!! |")
    print("|--------------------|")
    print(Style.RESET_ALL)
else:
    print(Fore.RED)
    print("|------------------|")
    print("| Compile Error... |")
    print("|------------------|")
    print(Style.RESET_ALL)

# execution time
print(Fore.YELLOW +
      f'Execution time : {(end-start):.2f} seconds\n', Style.RESET_ALL)
