valid_sums = [[1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [1, 4, 22, 19, 10, 25, 28, 31, 34, 37, 13, 40, 43, 16, 49, 52, 46], [1, 8, 30, 31, 35, 38, 41, 37]]


def get_k_child(n, k):

    total = 0

    for digit in repr(n):
        total += int(digit)**k

    return total


def is_ephemeral(n, k):

    sequence = [n]

    while n != 1:
        n = get_k_child(n,k)
        if n in sequence:
            sequence.append(n)
            break
        sequence.append(n)

    return sequence[-1] == 1


def count_ephemeral(n1, n2, k):

    count = 0

    for i in range(n1, n2):
        n_digit_sum = sum(map(int, str(i)))
        if n_digit_sum in valid_sums[k - 2]:
            if is_ephemeral(i, k):
                count += 1

    return count


print(count_ephemeral(1,10000,2))
