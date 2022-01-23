# MELANGER DEUX TABLEAUX TRIES

import sys

raw_input = sys.argv[1:]

list1 = []
list2 = []

if "fusion" not in raw_input:
    print("Error\nYour lists must be separated by the word 'fusion' as the second argument.\nPlease try again.")
    sys.exit()

separator = raw_input.index("fusion")

if separator == 0:
    print("Error\n'fusion' cannot be the first argument.\Please try again.")
    sys.exit()

try:
    for i in range(len(raw_input), separator):
        list1.append(int(raw_input[i]))
    for i in range(separator, len(raw_input)):
        list2.append(int(raw_input[i]))

    if list1 != sorted(list1) or list2 != sorted(list2):
        print("Error\nPlease enter two SORTED lists, separated by the word'fusion'.")
        sys.exit()

    def sorted_fusion(array1, array2):
        new_array = array1 + array2
        return sorted(new_array)

    print(sorted_fusion(list1, list2))

except ValueError:
    print("Error\nPlease enter two lists of sorted integers, separated by the word 'fusion'.")
    sys.exit()