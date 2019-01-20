import math

def worstCaseArrayOfSize(n):
    if n == 1:
        return [1]
    else:
        top = worstCaseArrayOfSize(int(math.floor(float(n) / 2)))
        bottom = worstCaseArrayOfSize(int(math.ceil(float(n) / 2)))
        return map(lambda x: x * 2, top) + map(lambda x: x * 2 - 1, bottom)

worstCaseArrayOfSize(8)