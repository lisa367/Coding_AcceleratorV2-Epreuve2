# CONTROLE DE PASS SANITAIRE

import sys

input = sys.argv[1: -1]
element = sys.argv[-1]

def filter(array, string):
    result_set = []
    for item in array:
        if string not in item.lower():
            result_set.append(item)
        else:
            continue
    if len(result_set) == 0:
        print(f"No {element} match found in the given set.")
    return result_set

if len(sys.argv) < 3:
    print("Error\nYou need to enter at least two arguments.\nPlease try again.")
    sys.exit()
else:
    print(filter(input, element))

#print(input, element, sep='\n')