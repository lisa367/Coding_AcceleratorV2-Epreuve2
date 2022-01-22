# INSERTION DANS UN TABLEAU TRIE

import sys

input = sys.argv[1: -1]
liste = [int(x) for x in input]
element = int(sys.argv[-1])

liste.sort()

try:
    def sorted_insert(array, num):
        sorted_array = []
        for i in range(len(array)):
            if num >= array[i]:
                sorted_array.append(array[i])
                if num < array[i+1]:
                    sorted_array.append(num)
                    sorted_array += array[i+1:]
                    break

            else:
                sorted_array.append(num)
                sorted_array += array[i:]
                break
        return sorted_array
    
    print(sorted_insert(liste, element))

except ValueError:
    print("Error\nPlease enter integers only.")
    sys.exit()

'''print(element)
print(liste)'''