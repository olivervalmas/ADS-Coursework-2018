import time


def get_k_child_1(n, k):

    total = 0

    for digit in repr(n):
        total += int(digit)**k

    return total


def get_k_child_2(n, k):
    return sum(int(dig)**k for dig in str(n))


digit_powers = [[0,1,4,9,16,25,36,49,64,91],[0,1,8,27,64,125,216,343,512,729],[0,1,16,81,256,625,1296,2401,4096,6561]]


def get_k_child_3(n, k):

    total = 0

    for digit in repr(n):
        total += digit_powers[k-2][int(digit)]

    return total


start = time.time()
for i in range(1000000):
    get_k_child_1(i,3)
end = time.time()
print(end-start)

start = time.time()
for i in range(1000000):
    get_k_child_2(i,3)
end = time.time()
print(end-start)

start = time.time()
for i in range(1000000):
    get_k_child_3(i,3)
end = time.time()
print(end-start)

