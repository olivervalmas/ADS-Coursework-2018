def get_k_child(n, k):
    return sum(int(dig)**k for dig in str(n))


valid_sums = [[1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [1, 4, 22, 19, 10, 25, 28, 31, 34, 37, 13, 40, 43, 16, 49, 52, 46], [1, 8, 30, 31, 35, 38, 41, 37]]


def permute(c, s=""):
    if len(s) == len(c):
        return [s]
    else:
        variations = [s[0:i] + c[len(s)] + s[i:] for i in range(len(s) + 1)]
        permutations = [permute(c, e) for e in variations]
        return [x for y in permutations for x in y]


sequence = set()
ephemeral_numbers = set()


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

    master_list = list(range(n1, n2))
    output = []

    while master_list:

        number = master_list[0]
        n_digit_sum = sum(map(int, str(number)))

        if is_ephemeral(number, k) and n_digit_sum in valid_sums[k-2]:

            print("ephemeral: " + str(number))
            all_perms = list(set(permute(str(number))))

            for perm in all_perms:
                print("ephemeral: " + str(perm))
                try:
                    master_list.remove(int(perm))
                except:
                    pass

            output += all_perms

        else:
            master_list.remove(number)

    new = []
    for val in output:
        if n1 <= int(val) < n2:
            new.append(int(val))
    new.sort()
    return list(set(new))


print(len(count_ephemeral(0, 100000, 4)))
#print(permute("1000"))

