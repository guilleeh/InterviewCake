def solution(string):
    end = len(string) - 1
    for index, element in enumerate(string):
        if index <= end:
            temp = element
            string[index] = string[end]
            string[end] = temp
            end -= 1
        else:
            break

    return string


test_1 = ['H', 'e', 'l', 'l', 'o']
print(solution(test_1) == ['o', 'l', 'l', 'e', 'H'])

test_2 = ['N']
print(solution(test_2) == ['N'])

test_3 = ['E', 'v', 'e', 'n']
print(solution(test_3) == ['n', 'e', 'v', 'E'])
