import time
#q2test.py
"""test function for question 2 of the ADS assignment, 2018-19"""


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
    ephemeral_numbers = []

    for i in range(n1, n2):
        n_digit_sum = sum(map(int, str(i)))

        if n_digit_sum in valid_sums[k - 2]:
            if is_ephemeral(i, k):
                count += 1
                ephemeral_numbers.append(i)

    ephemeral_numbers.sort()
    return len(ephemeral_numbers)


def q2test():
    """tests for the function count_ephemeral"""
    correct = True
    result = count_ephemeral(1, 10, 2)
    if result != 2:
        correct = False
        print("test failed for n1=1, n2=10, k=2; correct result is 2, result obtained was ", result)
    result = count_ephemeral(1000, 10000, 3)
    if result != 91:
        correct = False
        print("test failed for n1=1000, n2=10000, k=3; correct result is 91, result obtained was ", result)
    result = count_ephemeral(123456, 654321, 4)
    if result != 376:
        correct = False
        print("test failed for n1=123456, n2=654321, k=4; correct result is 376, result obtained was ", result)
    if correct:
        print("all tests passed")

start = time.time()
q2test()
end = time.time()
print(end-start)
