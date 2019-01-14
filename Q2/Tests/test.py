def get_k_child(n, k):
    return sum(int(dig)**k for dig in str(n))


def count_ephemeral(n1, n2, k):

    ephemeral_numbers = []
    ephemeral_sequences = []

    for i in range(n1, n2):

        sequence = [i]
        n = get_k_child(i, k)

        while n != 1 and n not in sequence:
            sequence.append(n)
            n = get_k_child(n, k)

        sequence.append(n)

        if sequence[-1] == 1:
            ephemeral_numbers.append(i)
            ephemeral_sequences.append(sequence)

    file = open("ephemeral_numbers_" + str(k) +".txt", "w")

    sums = []

    for i in range(0, len(ephemeral_numbers)):
        file.write(str(ephemeral_numbers[i]))
        file.write("\n")

        s = str(sum(int(dig) for dig in str(ephemeral_numbers[i])))
        if s not in sums:
            sums.append(s)

        #file.write(str(ephemeral_sequences[i]))
        #file.write("\n")

    file.write(str(sums))
    file.close()

count_ephemeral(0,10000000,2)
#count_ephemeral(0,10000000,3)
#count_ephemeral(0,10000000,4)