def get_k_child(n,k):

    digits = [x for x in str(n)]

    output = 0

    for digit in digits:
        output += int(digit) ** k

    return output


def count_ephemeral(n1,n2,k):

    ephemeral_numbers = []
    count = 0

    for original_number in range(n1,n2):

        test = True

        if original_number in ephemeral_numbers:
            count += 1
            test = False

        if test:

            sequence = [original_number]
            n = original_number
            while n != 1:
                n = get_k_child(n, k)
                if n in ephemeral_numbers:
                    count += 1
                    break
                if n in sequence:
                    sequence.append(n)
                    break
                sequence.append(n)

            if sequence[len(sequence)-1] == 1:
                count += 1

            for i in sequence:
                if sequence[len(sequence) - 1] == 1:
                    if i not in ephemeral_numbers:
                        ephemeral_numbers.append(i)
            print(count)

    print(count)


count_ephemeral(123456, 654321, 4)
