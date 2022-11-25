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
        'back': ['id', 'number'],
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
        'front': ['kska', 'kbka', 'id'],
        'back': ['id', 'number', 'kbki', 'sub', 'string', 'kski'],
        'ops': [
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
