#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'CountCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING A
#  2. STRING B
#

def CountCharacters(A, B):
    total = 0
    chars = set(A)
    for i in B:
        if i in chars:
            total = total+1
    return total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    first_multiple_input = input().rstrip().split()

    A = first_multiple_input[0]

    B = first_multiple_input[1]

    charcount = CountCharacters(A, B)

    fptr.write(str(charcount) + '\n')

    fptr.close()
