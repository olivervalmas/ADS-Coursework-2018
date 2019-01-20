import time


def get_k_child(n, digit_powers):

    total = 0

    for digit in repr(n):
        total += digit_powers[int(digit)]

    return total


def count_ephemeral(n1, n2, k):

    digit_powers = [x ** k for x in range(0, 10)]

    ephemeral_dict = {x: 0 for x in range(1, 7*(9**k)+1)}

    sequence = set()
    count = 0

    for i in range(1, 7*(9**k)+1):

        sequence.add(i)
        duplicate = False

        while i is not 1 and not duplicate:

            i = get_k_child(i, digit_powers)

            if ephemeral_dict[i] == 0:
                duplicate = True

            if ephemeral_dict[i] == 1:
                i = 1

            elif i in sequence:
                duplicate = True

            else:
                sequence.add(i)

        if not duplicate:
            for number in sequence:
                ephemeral_dict[number] = 1

        else:
            for number in sequence:
                ephemeral_dict[number] = 0

        sequence.clear()

    for j in range(n1, n2):
        if ephemeral_dict[get_k_child(j, digit_powers)] == 1:
            count += 1

    return count

start = time.time()
print(count_ephemeral(1000,10000,3))
end = time.time()
print(end-start)