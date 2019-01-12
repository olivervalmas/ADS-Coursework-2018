import time


#possible idea: create list with all numbers in range then systematically remove them as they are known to be ephemeral

def k_child(n,k):
    digits = [x for x in str(n)]
    total = 0
    for digit in digits:
        total += int(digit)**k
    return total


def count_ephemeral(n1,n2,k):

    ephemeral_numbers = []
    go_to_ephemeral_numbers = []
    counter = 0

    for number in range(n2-1,n1-1,-1):

        test_number = True
        count = False

        if number in go_to_ephemeral_numbers:
            counter += 1
            test_number = False
            print("Skipping " + str(number) + " as it is known to be ephemeral")

        if test_number:

            sequence = [number]
            n = k_child(number, k)

            while n not in sequence:

                sequence.append(n)
                n = k_child(n,k)

                if n in go_to_ephemeral_numbers:
                    count = True

            sequence.append(n)

            for i in sequence:
                if i not in go_to_ephemeral_numbers and 1 in sequence:
                    go_to_ephemeral_numbers.append(i)

            if 1 in sequence:
                count = True

            if count:
                counter += 1
                ephemeral_numbers.append(number)

            #print(sequence)

    print("Ephemeral numbers: " + str(ephemeral_numbers))
    print("Count: " + str(counter))
    #print("Go to ephemeral numbers: " + str(go_to_ephemeral_numbers))

start = time.time()
count_ephemeral(123456,654321,4)
end = time.time()
print(end-start)
#count_ephemeral(123456, 654321, 4)





