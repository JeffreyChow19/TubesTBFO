def checkVar(var):
    angka = [i for i in range(48, 58)]
    upper = [i for i in range(65, 91)]
    lower = [j for j in range(97, 123)]
    abjad = upper + lower

    accepted_first = abjad
    accepted_first.append(ord('_'))
    accepted_first.append(ord('$'))
    accepted = accepted_first + angka

    if (ord(var[0]) not in accepted_first):
        return False

    for letter in var:
        if (ord(letter) not in accepted):
            return False

    return True


def checkExpr(token):
    tokens = token
    type1 = {
        'front': ['number', 'id', "kbka", "kska"],
        'back': ['number', 'id', "kbki", "kski"],
        'ops': [
            'mul',
            'div',
            'mod',
            'pow',
            'xor',
        ]
    }

    type2 = {
        'front': ['id', "kbka", "kska", 'number'],
        'back': ['number', 'id', 'kbki'],
        'ops': [
            'leq',
            'l',
            'g',
            'geq',
        ]
    }

    type5 = {
        'front': ['id', "kbka", "kska"],
        'back': ['id','number'],
        'ops': [
            'inc',
            'dec',
        ]
    }

    type6 = {
        'front': [''],
        'back': ['id'],
        'ops': [
            'notbit',
            'notb',
        ]
    }

    type7 = {
        'front': ['id', "kbka", "kska", 'kkka'],
        'back': ['id', 'string', 'true', 'false', 'number', 'kski', 'kbki', 'kkki', 'null'],
        'ops': [
            'is',
        ]
    }

    type8 = {
        'front': ['id', 'string', 'true', 'false', 'number', 'kbka', 'kska'],
        'back': ['id', 'string', 'true', 'false', 'number', 'null', 'kbki'],
        'ops': [
            'isstricteq',
            'notstricteq',
            'iseq',
            'isneq',
            'and',
            'or',
            'andb',
            'orb',
        ]
    }

    type9 = {
        'front' : ['kska', 'kbka', 'id'],
        'back' : ['id', 'number', 'kbki', 'sub', 'string', 'kski'],
        'ops' : [
            'peq',
            'meq',
            'muleq',
            'diveq'
        ]
    }
    type10 = {
        'front': ['string', 'number', 'id', "kbka", "kska"],
        'back': ['string', 'number', 'id', 'kbki'],
        'ops': [
            'sum',
        ]
    }

    type11 = {
        'front': ['number', 'id', "kbka", "kska", 'kbki', 'kski'],
        'back': ['number', 'id', 'kbki'],
        'ops': [
            'sub',
        ]
    }

    for i in range(len(tokens)):
        if tokens[i] in type1['ops']:
            try:
                if tokens[i - 1] not in type1['front'] or tokens[i + 1] not in type1['back']:
                    return i
            except:
                return i

        if tokens[i] in type2['ops']:
            try:
                if tokens[i - 1] not in type2['front'] or tokens[i + 1] not in type2['back']:
                    return i
            except:
                return i

        if tokens[i] in type5['ops']:
            try:
                if tokens[i - 1] not in type5['front']:
                    if tokens[i + 1] not in type5['back']:
                        return i
                if tokens[i + 1] not in type5['back']:
                    if tokens[i - 1] not in type5['front']:
                        return i
            except:
                return i

        if tokens[i] in type6['ops']:
            try:
                if tokens[i + 1] not in type6['back']:
                    return i
            except:
                return i

        if tokens[i] in type7['ops']:
            try:
                if tokens[i - 1] not in type7['front'] or tokens[i + 1] not in type7['back']:
                    return i
            except:
                return i

        if tokens[i] in type8['ops']:
            try:
                if tokens[i - 1] not in type8['front'] or tokens[i + 1] not in type8['back']:
                    return i
            except:
                return i

        if tokens[i] in type9['ops']:
            try:
                if tokens[i - 1] not in type9['front'] or tokens[i + 1] not in type9['back']:
                    return i
            except:
                return i

        if tokens[i] in type10['ops']:
            try:
                if tokens[i - 1] not in type10['front'] or tokens[i + 1] not in type10['back']:
                    return i
            except:
                return i

        if tokens[i] in type11['ops']:
            try:
                if tokens[i - 1] not in type11['front'] or tokens[i + 1] not in type11['back']:
                    return i
            except:
                return i

    return True

    '''
    Type 1 :
        Front   : string, number, id
        Back    : string, number, id
    
    Type 2 :
        Front   : id
        Back    : string, number, id

    Type 3 :
        Front   : id
        Back    : id

    Type 4 :
        Front   : number, id
        Back    : number, id

    Type 5 :
        Front   : id
        Back    : -

    Type 6 :
        Front   : -
        Back    : id

    '''

    '''
    # front and back could be anything
    isstricteq
    notstricteq
    iseq
    isneq
    sum
    sub
    mul
    div
    mod

    # front must id back could be anything
    leg
    l
    geq
    g
    peq
    meq
    is

    # front must id so must back
    and
    or

    # front must id/number so must back
    pow
    xor
    andb
    orb


    # front must id
    inc
    dec
    
    # back must id
    notbit
    notb


    dict = [
        {
            'type': 1,
            'front': ['string', 'number', 'id'],
            'back': ['string', 'number', 'id'],
            'ops':[
                'isstricteq',
                'notstricteq',
                'iseq',
                'isneq',
                'sum',
                'sub',
                'mul',
                'div',
                'mod'
            ]
        },
        {
            'type': 2,
            'front': ['id'],
            'back': ['string', 'number', 'id'],
            'ops':[
                'leg'
                'l',
                'geq',
                'g',
                'peq',
                'meq',
                'is'
            ]
        },
        {
            'type': 3,
            'front': ['id'],
            'back': ['id'],
            'ops':[
                'and',
                'or'
            ]
        },
        {
            'type': 4,
            'front': ['id', 'number'],
            'back': ['id', 'number'],
            'ops':[
                'pow',
                'xor',
                'andb',
                'orb'
            ]
        },
        {
            'type': 5,
            'front': ['id'],
            'back': [],
            'ops':[
                'inc'
                'dec'
            ]
        },
        {
            'type': 6,
            'front': [],
            'back': ['id'],
            'ops':[
                'notbit',
                'notb'
            ]
        }
    ]


    # mid_operators = ["isstricteq", "notstricteq",
    #                  "iseq", "isneq", "leq", "l", "geq", "g", "and", "or", "pow", "peq", "meq", "xor", "andb", "orb", "is", "sum", "sub", "mul", "div", "mod"]

    # opFirst = [
    #     "notbit",
    #     "notb",
    # ]

    # opLast = [
    #     "inc",
    #     "dec",
    # ]

    # operateableType = ["string", "number", "id"]

    operators = ['isstricteq', 'notstricteq', 'iseq', 'isneq', 'sum', 'sub', 'mul', 'div', 'mod', 'legl',
                'geq', 'g', 'peq', 'meq', 'is', 'and', 'or', 'pow', 'xor', 'andb', 'orb', 'incdec', 'notbit', 'notb']


    '''


# answer = checkExpr(['let', 'id', 'is', 'id', 'sum', 'id',
#                    'sum', 'id', 'newline', 'id', 'is', 'id', 'and', 'id'])

# if answer != True:
#     print('hello')
# else:
#     print('kntl')
