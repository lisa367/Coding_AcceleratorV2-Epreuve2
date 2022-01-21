# CONCAT

import sys

separator = sys.argv[-1]
def concatenator():
    liste = sys.argv[1: -1]
    str = separator.join(liste)
    return str

print(concatenator())