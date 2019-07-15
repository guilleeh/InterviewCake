def solution(array):
    # We sort by start time
    array.sort()
    new_array = []
    # We create new list with the earliest start time
    if len(array) > 1:
        new_array.append(array[0])
    else:
        return array

    for i, element in enumerate(array):
        if i != 0:
            if new_array[-1][1] >= array[i][0]:
                new_array[-1] = (new_array[-1][0],
                                 max(new_array[-1][1], array[i][1]))
            else:
                new_array.append(element)
    return new_array


'''
Time complexity: O(N Log N), since we are first sorting the array, and then we have to iterate through it one more time.
Space Complexity: O(N), in the worst case, none of the meetings overlap so we would have to add them all to our new array.
'''


case_1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(solution(case_1))
print()


case_2 = [(1, 2), (2, 3)]
print(solution(case_2))
print()

case_3 = [(1, 5), (2, 3)]
print(solution(case_3))
print()


case_4 = [(1, 10), (2, 6), (3, 5), (7, 9)]
print(solution(case_4))
print()
