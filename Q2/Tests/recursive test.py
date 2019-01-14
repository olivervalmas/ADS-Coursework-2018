import time

valid_sums = [[1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [1, 4, 22, 19, 10, 25, 28, 31, 34, 37, 13, 40, 43, 16, 49, 52, 46], [1, 8, 30, 31, 35, 38, 41, 37]]


def get_k_child(n, k):

    digit_powers = [x**k for x in range(0, 10)]
    total = 0

    for digit in repr(n):
        total += digit_powers[int(digit)]

    return total


sequence = set()
leads_to_ephemeral = set()
leads_to_eternal = set()


def check_ephemeral(n, k):

    if sum(map(int, str(n))) not in valid_sums[k-2]:
        sequence.clear()
        return False

    elif n in leads_to_eternal or n in sequence:

        for i in sequence:
            if i < 10000:
                leads_to_eternal.add(i)

        sequence.clear()
        return False

    if n == 1:
        sequence.add(1)

    if n == 1 or n in leads_to_ephemeral:

        for i in sequence:
            if i < 10000:
                leads_to_ephemeral.add(i)

        sequence.clear()
        return True

    else:
        sequence.add(n)
        return check_ephemeral(get_k_child(n, k), k)


def count_ephemeral(n1, n2, k):

    count = 0

    for i in range(n1, n2):
        n_digit_sum = sum(map(int, str(i)))
        if n_digit_sum in valid_sums[k - 2]:
            if check_ephemeral(i, k):
                count += 1

    return count


start = time.time()
print(count_ephemeral(123456, 654321, 4))
end = time.time()
print(end-start)