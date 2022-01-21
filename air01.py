# SPLIT EN FOMCTION

import sys

try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    def splitter(string=input1, separator=' '):
        new_str = string.replace(input2, '\n')
        return(new_str)


    print(splitter(input1, input2))

except IndexError:
    print("Erreur\nVous avez oublié le deuxième argument.")