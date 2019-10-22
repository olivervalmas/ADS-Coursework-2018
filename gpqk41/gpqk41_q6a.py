def merge(left, right):

    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
        elif len(left) > 0:
            result += left
            left = []
        else:
            result += right
            right = []

    return result


def selection_sort(input_list):
    n = len(input_list)
    for i in range(0, n):
        elem = input_list[i]
        pos = i
        for j in range(i+1, n):
            if input_list[j] >= elem:
                elem = input_list[j]
                pos = j
        temp = input_list[i]
        input_list[i] = input_list[pos]
        input_list[pos] = temp
    return input_list


def hybrid_sort(input_list):

    if len(input_list) <= 4:
        return selection_sort(input_list)

    middle = int(len(input_list) / 2)

    left = input_list[:middle]
    right = input_list[middle:]

    left_sorted = hybrid_sort(left)
    right_sorted = hybrid_sort(right)

    return merge(left_sorted, right_sorted)
