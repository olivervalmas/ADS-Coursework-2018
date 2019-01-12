import time


def get_k_child(n, k):
    return sum(int(dig)**k for dig in str(n))


sequence = set()
ephemeral_numbers = set()
# valid sums for k = 2, 3, 4
valid_sums = [[1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [1, 4, 22, 19, 10, 25, 28, 31, 34, 37, 13, 40, 43, 16, 49, 52, 46], [1, 8, 30, 31, 35, 38, 41, 37]]


def is_ephemeral(n, k):

    if n == 1 or n in ephemeral_numbers:

        for i in sequence:
            ephemeral_numbers.add(i)

        sequence.clear()
        return True

    elif n in sequence:
        sequence.clear()
        return False

    else:
        sequence.add(n)
        return is_ephemeral(get_k_child(n, k), k)


def count_ephemeral(n1, n2, k):

    count = 0

    for i in range(n1, n2):

        n_digit_sum = sum(map(int, str(i)))

        if n_digit_sum in valid_sums[k - 2]:
            if is_ephemeral(i, k):
                count += 1

    return count


times = []
n = 0

while n < 1:

    start = time.time()
    print(count_ephemeral(123456, 654321, 4))
    end = time.time()
    times.append(end-start)
    n += 1

print(sum(times)/len(times))