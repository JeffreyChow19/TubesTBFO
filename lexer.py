import re
import FA
import sys
from colorama import Fore, Style

# Style
class Format:
    end = '\033[0m'
    underline = '\033[4m'

tokenCollection = [
    # Tuples for defining JS syntax to GRAMMAR

    # IGNORE TYPES
    (r'[ \t]+',                                 None), 
    (r'//[^\n]*',                               None),
    (r'/\*[^\n]+[ \t]*[//]*[\w\W]*[$\n]*\*/',   None),

    # DATA TYPES
    (r'\"[^\"\n]*\"',               "string"),
    (r'\'[^\'\n]*\'',               "string"),
    (r'\bvar\b',                    "var"),
    (r'\blet\b',                    "let"),
    (r'\bconst\b',                  "const"),

    # SYNTAX
    (r'\bfunction\b',           "function"),
    (r'\breturn\b',             "return"),
    (r'\bif\b',                 "if"),
    (r'\belse\b',               "else"),
    (r'\bfor\b',                "for"),
    (r'\bof\b',                 "of"),
    (r'\bwhile\b',              "while"),
    (r'\bcontinue\b',           "continue"),
    (r'\bbreak\b',              "break"),
    (r'\btrue\b',               "true"),
    (r'\bfalse\b',              "false"),
    (r'\bnull\b',               "null"),
    (r'\bswitch\b',             "switch"),
    (r'\bcase\b',               "case"),
    (r'\bdefault\b',            "default"),
    (r'\btry\b',                "try"),
    (r'\bcatch\b',              "catch"),
    (r'\bthrow\b',              "throw"),
    (r'\bfinally\b',            "finally"),
    (r'\bthrow\b',              "throw"),
    (r'\bimport\b',             "import"),
    (r'\bfrom\b',               "from"),
    (r'\bexport\b',             "export"),
    (r'\bdelete\b',             "delete"),
    (r'\btypeof\b',             "typeof"),
    (r'\bin\b',                 "in"),
    (r'\binstanceof\b',         "instanceof"),
    (r'\bInfinity\b',           "infinity"),
    (r'\bin\b',                 "in"),
    (r'\bof\b',                 "of"),
    (r'\bas\b',                 "as"),

    # ESCAPE SEQUENCE
    (r'\n',              "newline"),
    (r'\(',              "kbki"),  # kurung biasa kiri
    (r'\)',              "kbka"),  # kurung biasa kanan
    (r'\{',              "kkki"),  # kurung kurawal kiri
    (r'\}',              "kkka"),  # kurung kurawal kanan
    (r'\[',              "kski"),  # kurung siku kiri
    (r'\]',              "kska"),  # kurung siku kanan
    (r'\:',              "td"),  # titik dua
    (r'\;',              "tk"),  # titik koma
    (r'\,',              "km"),  # koma

    # Operator (boolean)
    (r'\===',            "isstricteq"),
    (r'\!==',            "notstricteq"),
    (r'\==',             "iseq"),
    (r'\!=',             "isneq"),
    (r'\<=',             "leq"),
    (r'<',               "l"),  # less
    (r'>=',              "geq"),
    (r'>',               "g"),  # greater
    (r'&&',              "and"),  # and boolean
    (r'\|\|',            "or"),  # or boolean
    (r'\!',              "notb"),  # not boolean
    # ternary (dipasangkan dengan :) e.g. x = expr1 ? val1 : val2
    (r'\?',              "qb"),

    # Operator (arithmetic)
    (r'\*\*',             "pow"),
    (r'\+\=',             "peq"),  # plus equal
    (r'\-\=',             "meq"),  # minus equal
    (r'\*\=',             "muleq"),  # multiply equal
    (r'\/\=',             "diveq"),  # div equal
    (r'\+\+',             "inc"),  # increment
    (r'\-\-',             "dec"),  # decrement
    (r'\^',               "xor"),
    (r'&',                "andb"),  # and bitwise
    (r'\|',               "orb"),  # or bitwise
    (r'\=',               "is"),  # assigment
    (r'\+',               "sum"),  # sum , concat str
    (r'\-',               "sub"),
    (r'\*',               "mul"),
    (r'/',                "div"),
    (r'%',                "mod"),
    (r'~',                "notbit"),

    # Var Name, Class method, Obj Props
    (r'\.',                                                      "titik"),
    (r'[0-9]*[\$]*[a-zA-Z_][a-zA-Z0-9_]*',                       "id"),
    (r'[\+\-]?[0-9]+\.[0-9]+',      "number"),
    (r'[\+\-]?[0-9]+[e-]?[0-9]*',   "number"),
    (r'[\+\-]?[0-9]+',              "number"),
]


def lexer(text, tokenCollection):
    currentPos = 1  # position in current line
    currentLine = 1  # current line
    usedTokens = []
    pointerText = 0  # text pointer
    endLoop = False
    while(pointerText < len(text) and not endLoop):
        if text[pointerText] == '\n':
            currentLine += 1
            currentPos = 1

        match = None
        for tokenExpr in tokenCollection:
            pattern, tokenTag = tokenExpr

            regex = re.compile(pattern)  # init regex
            # check till current pointer
            match = regex.match(text, pointerText)

            if match:  # check matcher
                if tokenTag:  # get token
                    currentTokens = tokenTag
                    if (currentTokens == "id"):
                        if (FA.checkVar(match.group(0))):
                            usedTokens.append(currentTokens)
                        else:
                            endLoop = True
                            break
                    else:
                        usedTokens.append(currentTokens)
                break

        if not match:  
            endLoop = True
            break
        else:  # set current text pointer to end of current match position
            # set pointer to end of current match position
            pointerText = match.end(0)

        currentPos += 1
    counterNewLine = 1
    foundErrorLine = False
    currentLineStr = ""
    indexError = 0
    if (endLoop):
        for i in range(len(text)):
            if (text[i] == '\n' and not foundErrorLine):
                counterNewLine += 1
            else:
                if (counterNewLine == currentLine):
                    if (text[i] == '\n' or i == len(text)):
                        break
                    else:
                        if text[i] == text[pointerText]:
                            indexError = i
                        foundErrorLine = True
                        currentLineStr += text[i]
        print()
        print(Fore.RED, end="")
        print("|------------------|")
        print("| Syntax Error !!! |")
        print("|------------------|")
        print(Style.RESET_ALL, end="")
        print("\n>>> Line " + str(currentLine) + " : " +  "\"", end="")
        for j in range(len(currentLineStr)):
            if j == indexError:
                print(Fore.RED, end="")
                print(Format.underline + "" + currentLineStr[j] + Format.end, end="")
                print(Style.RESET_ALL, end="")
            else:
                print(Fore.GREEN, end="")
                print(currentLineStr[j], end="")
                print(Style.RESET_ALL, end="")
        print("\".\n")
        print()
        sys.exit(1)
    else:
        if (FA.checkExpr(usedTokens) == True):
            return usedTokens
        else:
            currentNewline = 0
            errorIndex = FA.checkExpr(usedTokens)
            newlineCounter = 0
            for i in range(errorIndex):
                if (usedTokens[i] == 'newline'):
                    newlineCounter += 1

            i = 0
            while (currentNewline < newlineCounter):
                if (text[i] == '\n'):
                    currentNewline += 1
                i += 1

            while (text[i] != '\n'):
                currentLineStr += text[i]
                i += 1
            currentNewline += 1
            print()
            print(Fore.RED, end="")
            print("|------------------------|")
            print("| Invalid Expression !!! |")
            print("|------------------------|")
            print(Style.RESET_ALL, end="")
            print("\n>>> Line " + str(currentNewline) + " : ", end="")
            print(Fore.RED, end="")
            print(Format.underline + "\"" + currentLineStr + "\"." + Format.end, end="")
            print(Style.RESET_ALL)
            print()
            sys.exit(1)


def parseToToken(path):
    file = open(path)
    text = file.read()
    file.close()

    usedTokens = lexer(text, tokenCollection)
    tokenInText = []
    for token in usedTokens:
        tokenInText.append(token)
    resultToken = list(filter(lambda x: x != 'newline', tokenInText))
    return resultToken