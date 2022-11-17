import re
import sys

tokenCollection = [
    # Tuples for defining JS syntax to GRAMMAR
    
    # IGNORE TYPES
    (r'[ \t]+',                        None), # ignore spaces at left
    (r'//[^\n]*',          None),
    # (r'/\*[^\n]*[ \t]*[//]*[\w\W]*\*/',     None), 
    (r'/\*[^\n]+[ \t]*[//]*[\w\W]*[$\n]*\*/',     None),
    # (r'[ \t]*[\n]+',                  "newline"), # ignore space+repeated \n or space

    # DATA TYPES
    (r'\"[^\w]\"',  "string"),
    # (r''),


    # SYNTAX
    (r'\bfunction\b',    "function"),
    (r'\bif\b',          "if"),
    (r'\belse\b',        "else"),
    (r'\belse if\b',     "else if"),


    # ESCAPE SEQUENCE
    (r'\n',              "newline"),
    (r'\(',              "kbki"), # kurung biasa kiri
    (r'\)',              "kbka"), # kurung biasa kanan
    (r'\{',              "kkki"), # kurung kurawal kiri
    (r'\}',              "kkka"), # kurung kurawal kanan
    (r'\[',              "kski"), # kurung siku kiri
    (r'\]',              "kska"), # kurung siku kanan
    (r'\:',              "colon"), # titik dua
    (r'\;',              "scolon"), # titik koma

    # Operator
    (r'\===',            "isstricteq"),
    (r'\==',             "iseq"),
    (r'\!=',             "isneq"),
    (r'\<=',            "leq"),
    (r'\<',             "l"),
    (r'\>=',             "geq"),
    (r'\>',             "g"),
    (r'\>=',             "geq"),
]

def lexer(text, tokenCollection):
    currentPos = 1 # position in current line
    currentLine = 1 # current line
    usedTokens = []
    pointerText = 0 # text pointer
    while(pointerText < len(text)):
        if text[pointerText] == '\n':
            currentLine += 1
            currentPos = 1

        match = None

        for tokenExpr in tokenCollection:
            pattern , tokenTag = tokenExpr

            regex = re.compile(pattern) # init regex
            match = regex.match(text, pointerText) # check till current pointer

            if match: # check matcher
                if tokenTag: # get token
                    currentTokens = tokenTag
                    usedTokens.append(currentTokens)
                break

        if not match: # throws error if not match
            print(f"\nSyntax Error!\nLine: {currentLine},{currentPos} (character: {text[pointerText]})")
            sys.exit(1)
        else: # set current text pointer to end of current match position
            pointerText = match.end(0) # set pointer to end of current match position

        currentPos += 1
    print(usedTokens)
    return usedTokens

def parseTextToken(path):
    file = open(path)
    text = file.read()
    file.close()

    usedTokens = lexer(text, tokenCollection)
    tokenInText = []
    for token in usedTokens:
        tokenInText.append(token)

    return tokenInText

parseTextToken('TC1.txt')

