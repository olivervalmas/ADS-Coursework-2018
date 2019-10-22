def hash_double(input):

    hash_table = ["-"] * 19

    for k in input:

        position = (6 * k + 3) % 19
        collisions = 0

        while hash_table[position] != "-":

            position = (position + (11 - k % 11)) % 19
            collisions += 1

            if collisions == 19:
                return hash_table

        hash_table[position] = k

    return hash_table


def hash_quadratic(input):

    hash_table = ["-"]*19

    for k in input:

        position = (6 * k + 3) % 19
        collisions = 1

        while hash_table[position] != "-":

            position = (position - (collisions-1)**2 + collisions**2)%19

            collisions += 1

            if collisions == 100:
                break

        if collisions != 100:
            hash_table[position] = k

    return hash_table

def test_dh():
    assert hash_double([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_double([19,38,57,76,95,114,133,152,171,190,209,228,247,266,285,304,323,342,361]) == [304, 361, 266, 19, 76, 152, 228, 95, 171, 38, 114, 190, 57, 133, 209, 247, 285, 323, 342]
    assert hash_double([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 67, 3, 19, 53, 13, 29, 7, 23, 59, 17, 41, 11, 61, 5, 2, 37, 43, 31]
    print("all tests passed")


def test_hq():
    assert hash_quadratic([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [9, 6, 3, 19, 16, 13, 10, 7, 4, 1, 17, 14, 11, 8, 5, 2, 18, 15, 12]
    assert hash_quadratic([19,38,57,76,95,114,133,152,171,190]) == [95, 133, '-', 19, 38, '-', '-', 57, 190, 114, 171, '-', 76, '-', 152, '-', '-', '-', '-']
    assert hash_quadratic([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]) == [47, 71, 3, 19, 43, 13, 29, 7, 23, 61, 17, 41, 11, 59, 5, 2, 37, 53, 31]
    print("all tests passed")


test_dh()
test_hq()