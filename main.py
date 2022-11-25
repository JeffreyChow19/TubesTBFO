import CFG
import CYK
import lexer
import argparse
import time
from colorama import Fore, Back, Style


def splash():
    print(Fore.YELLOW)
    print("============")
    print("三位棉兰男神")
    print("============")
    print(Style.RESET_ALL)


# splash screen
splash()

# argparse
# try:
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()
filename = args.file.name

print(Fore.BLUE +
        f'Checking {filename}...\nPlease wait for a moment...' + Style.RESET_ALL)

start = time.time()
# grammar
grammar = CFG.Grammar().parseCFG('grammar.txt')

# lexer
lexer = lexer.parseToToken(filename)

# CYK algorithm
result = CYK.cykParse(lexer, grammar)

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

print(Fore.YELLOW +
        f'Execution time : {(end-start):.2f} seconds\n', Style.RESET_ALL)

# except:
#     print(Fore.RED + "\nFile not found :)\n" + Style.RESET_ALL)
