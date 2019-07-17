def solution(array_1, array_2):
    # Naive implementation
    # array_1.extend(array_2)
    # array_1.sort()
    # return array_1

    total_length = len(array_1) + len(array_2)
    sorted_array = [None] * total_length

    sorted_index = 0
    first_array_index = 0
    second_array_index = 0

    while sorted_index < total_length:
        first_array_done = first_array_index > len(array_1) - 1
        second_array_done = second_array_index > len(array_1) - 1

        if not first_array_done and (second_array_done or array_1[first_array_index] < array_2[second_array_index]):
            sorted_array[sorted_index] = array_1[first_array_index]
            first_array_index += 1
        else:
            sorted_array[sorted_index] = array_2[second_array_index]
            second_array_index += 1

        sorted_index += 1

    return sorted_array


case_1 = [3, 4, 6, 10, 11, 15]
case_1_2 = [1, 5, 8, 12, 14, 19]

print(solution(case_1, case_1_2) == [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])
print(solution(case_1, case_1_2))
