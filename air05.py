# UN SEUL A LA FOIS

import sys

if len(sys.argv) > 2:
    print("Erreur\nCe programme n'accepte qu'un seul argument.\nVotre chaîne de caractères se trouve-t-elle bien entre guillemets ?\n")
    sys.exit()

input = sys.argv[1]
new_str = ""
for i in range(len(input)-1):
    if input[i] == input[i+1]:
        continue
    else:
        new_str += input[i]
new_str += input[-1]

print(new_str)