def get_k_child(n, digit_powers):

    total = 0

    for digit in repr(n):
        total += digit_powers[int(digit)]

    return total


def count_ephemeral(n1, n2, k):

    digit_powers = [x**k for x in range(0, 10)]

    ephemeral = set()
    eternal = set()
    sequence = set()
    count = 0

    for i in range(n1, n2):

            duplicate = False

            while i is not 1 and not duplicate:
                i = get_k_child(i, digit_powers)

                if i in eternal:
                    duplicate = True

                if i in ephemeral:
                    i = 1

                elif i in sequence:
                    duplicate = True

                else:
                    sequence.add(i)

            if not duplicate:
                for number in sequence:
                    ephemeral.add(number)
                count += 1
            else:
                for number in sequence:
                    eternal.add(number)

            sequence.clear()

    return count
