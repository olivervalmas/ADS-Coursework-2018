import time


def get_k_child(n, k):

    digit_powers = [x**k for x in range(0, 10)]
    total = 0

    for digit in repr(n):
        total += digit_powers[int(digit)]

    return total


def count_ephemeral(n1, n2, k):

    ephemeral = set()
    eternal = set()
    sequence = set()
    count = 0

    valid_sums = [
        [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
         32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58],
        [1, 4, 22, 19, 10, 25, 28, 31, 34, 37, 13, 40, 43, 16, 49, 52, 46], [1, 8, 30, 31, 35, 38, 41, 37]]

    for i in range(n1, n2):


            duplicate = False

            while i is not 1 and not duplicate:
                i = get_k_child(i, k)

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


start = time.time()
print("Time for 1 to 10 million for k=2: " + str(count_ephemeral(1,10000000,2)))
end = time.time()
print(end-start)

start = time.time()
print("Time for 1 to 10 million for k=3: " + str(count_ephemeral(1,10000000,3)))
end = time.time()
print(end-start)

start = time.time()
print("Time for 1 to 10 million for k=4: " + str(count_ephemeral(1,10000000,4)))
end = time.time()
print(end-start)

