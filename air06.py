# SUR CHACUN D'ENTRE EUX

import sys

try:
    operation = sys.argv[-1]
    operateur = operation[0]
    y = int(operation[1:])
    input = sys.argv[1: -1]

    if operateur == "+":
        result_set = [int(x)+y for x in input]
        print(result_set)
    elif operateur == "-":
        result_set = [int(x)-y for x in input]
    else:
        print("N'avez-vous pas oublié l'opérateur ou bien les guillemets pour le dernier argument ?\nRéessayez.")
        sys.exit()
    
    #print(result_set)

except ValueError:
    print("Erreur")
    sys.exit()
