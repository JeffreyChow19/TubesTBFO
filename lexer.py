import re
import sys

tokenCollection = [
    # Tuples for defining JS syntax to GRAMMAR

    # IGNORE TYPES
    (r'[ \t]+',                                 None),  # ignore spaces at left
    (r'//[^\n]*',                               None),
    (r'/\*[^\n]+[ \t]*[//]*[\w\W]*[$\n]*\*/',   None),

    # DATA TYPES
    (r'\"[\w]*[\W]*\"',                    "string"),
    (r'\'[\w]*\'',                  "string"),
    (r'[\+\-]?[0-9]+\.[0-9]+',      "number"),
    (r'[\+\-]?[0-9]+[e-]?[0-9]*',   "number"),
    (r'[\+\-]?[0-9]+',              "number"),
    (r'\bvar\b',                    "var"),
    (r'\blet\b',                    "let"),
    (r'\bconst\b',                  "const"),


    # SYNTAX
    (r'\bfunction\b',           "function"),
    (r'\breturn\b',             "return"),
    (r'\bif\b',                 "if"),
    (r'\belse\b',               "else"),
    (r'\belse if\b',            "else if"),
    (r'\bfor\b',                "for"),
    (r'\bwhile\b',              "while"),
    (r'\bcontinue\b',           "continue"),
    (r'\bbreak\b',              "break"),
    (r'\btrue\b',               "true"),
    (r'\bfalse\b',              "false"),
    (r'\bnull\b',               "null"),
    (r'\bexport default\b',     "export default"),
    (r'\bswitch\b',             "switch"),
    (r'\bcase\b',               "case"),
    (r'\bdefault\b',            "default"),
    (r'\btry\b',                "try"),
    (r'\bcatch\b',              "catch"),
    (r'\bthrow\b',              "throw"),
    (r'\bfinally\b',            "finally"),
    (r'\bthrow\b',              "throw"),
    (r'\bimport\b',             "import"),
    (r'\bexport\b',             "export"),
    (r'\bdelete\b',             "delete"),
    (r'\btypeof\b',             "typeof"),
    (r'\bin\b',                 "in"),
    (r'\binstanceof\b',         "instanceof"),
    (r'\bInfinity\b',           "Infinity"),
    (r'\bin\b',                 "in"),

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


    # Var Name, Class method, Obj Props
    (r'[a-zA-Z_][a-zA-Z0-9_]*[\.][a-zA-Z_][a-zA-Z0-9_]*',        "kartitik"),
    (r'\.',                                                      "titik"),
    (r'[a-zA-Z_][a-zA-Z0-9_]*',                                  "id"),
]


def lexer(text, tokenCollection):
    currentPos = 1  # position in current line
    currentLine = 1  # current line
    usedTokens = []
    pointerText = 0  # text pointer
    while(pointerText < len(text)):
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
                    usedTokens.append(currentTokens)
                break

        if not match:  # throws error if not match
            print(
                f"\nSyntax Error!\nLine: {currentLine},{currentPos} (character: {text[pointerText]})")
            sys.exit(1)
        else:  # set current text pointer to end of current match position
            # set pointer to end of current match position
            pointerText = match.end(0)

        currentPos += 1
    print(usedTokens)
    return usedTokens


def parseToToken(path):
    file = open(path)
    text = file.read()
    file.close()

    usedTokens = lexer(text, tokenCollection)
    tokenInText = []
    for token in usedTokens:
        tokenInText.append(token)

    return tokenInText


# parseTextToken('test/TC1.txt')
