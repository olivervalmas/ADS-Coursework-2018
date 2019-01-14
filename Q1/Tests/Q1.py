def hash_double(input):
    table = ["-"] * 19

    for k in input:

        i = (6 * k + 3) % 19
        count = 0

        while table[i] != "-":

            i = (i + (11 - k % 11)) % 19
            count += 1

            if count == 19:
                return table

        table[i] = k

    return table

expected = [47, 71, 3, 19, 43, 13, 29, 7, 23, 61, 17, 41, 11, 59, 5, 2, 37, 53, 31]

def hash_quadratic(input):

    table = ["-"]*19

    for k in input:

        #print("attempting to hash: " + str(k))
        i = (6*k + 3)%19
        collisions = 1

        while table[i] != "-":

            i = (i - (collisions-1)**2 + collisions**2)%19

            collisions += 1
            print(collisions)

            if collisions == 100:
                print("infinite loop")
                break

        if collisions != 100:
            table[i] = k

        print(table)

    return table




print(hash_quadratic([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]))
print(expected)
