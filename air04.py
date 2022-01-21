# CHERCHER L'INTRUS

import sys

def intrus(liste):
    sans_intrus = []
    for item in liste:
        if liste.count(item) == 1:
            sans_intrus.append(item)
        else:
            continue
    return '\n'.join(sans_intrus)

print(intrus(sys.argv[1:]))