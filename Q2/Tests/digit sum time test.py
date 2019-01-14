import time


def get_n_digit_sum_1(n):

    total = 0

    for digit in repr(n):
        total += int(digit)

    return total


def get_n_digit_sum_2(n):
    return sum(map(int, str(i)))


start = time.time()
for i in range(5000000):
    get_n_digit_sum_1(i)
end = time.time()
print(end-start)

start = time.time()
for i in range(5000000):
    get_n_digit_sum_2(i)
end = time.time()
print(end-start)
