# SPLIT

import sys

input = sys.argv[1]
if len(sys.argv) <= 2:
    tableau = input.split(' ')
    print('\n'.join(tableau))
else:
    print("Erreur\nCe programme n'accepte qu'un seul argument.\nVotre chaîne de caractères se trouve-t-elle bien entre guillemets ?\n")
    sys.exit()