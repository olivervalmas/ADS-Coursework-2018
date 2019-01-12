def merge_sort(input_list):

    if len(input_list) <= 1:
        return input_list

    middle = int(len(input_list) / 2)

    left = input_list[:middle]
    right = input_list[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):

    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result += left
            left = []
        else:
            result += right
            right = []

    return result



