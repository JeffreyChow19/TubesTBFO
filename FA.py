def checkVar(var):
    angka = [i for i in range(48, 58)]
    upper = [i for i in range(65, 91)]
    lower = [j for j in range(97, 123)]
    abjad = upper + lower

    accepted_first = abjad
    accepted_first.append(ord('_'))

    accepted = accepted_first + angka

    if (ord(var[0]) not in accepted_first):
        return False

    for letter in var:
        if (ord(letter) not in accepted):
            return False

    return True


# def checkExpr(tokens):
#     operators = ["isstricteq", "notstricteq",
#                  "iseq", "isneq", "leq", "l", "geq", "g", "and"]
#     pass
