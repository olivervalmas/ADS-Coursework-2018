#AJ Sung Q1 ADS Summative check generator

from random import *

def randomList():
    list = []
    for x in range(randrange(1, 25, 1) ):
        list.append(x)

    return list

file = open('Q1_Batch_Test.py', 'w')

file.write('#AJ Sung Q1 ADS Summative check generator\n')

file.write('from Q1 import *\n')

file.write('\ndef test_hq():')

for x in range(5000):
    currentList = randomList()

    file.write('\n    assert hash_quadratic([')
    for m in currentList:
        file.write(str(m)+", ")
    file.write("]) ==")

    file.write(' [')

    quadratic = hash_quadratic(currentList)
    for m in quadratic:
        if m == "-":
            file.write('"-", ')
        else:
            file.write(str(m)+", ")
    file.write("]")

file.write('\n    print ("all Quadratic Probing tests passed")\n')

file.write('\ndef test_dh():\n')

for x in range(5000):
    currentList = randomList()

    file.write('\n    assert hash_double([')
    for m in currentList:
        file.write(str(m)+", ")
    file.write("]) ==")

    file.write(' [')

    quadratic = hash_quadratic(currentList)
    for m in quadratic:
        if m == "-":
            file.write('"-", ')
        else:
            file.write(str(m)+", ")
    file.write("]")

file.write('\n    print ("all Hashing tests passed")\n')



file.write('test_hq()\n')
file.write('test_dh()\n')

file.close()

