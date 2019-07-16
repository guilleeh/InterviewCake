
def reverse(word, start, end):
    '''
    Reverses a string array
    '''
    while start < end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1

    print(word)


def solution(array):
    # Reverse current string array
    reverse(array, 0, len(array)-1)

    start_index = 0
    for i in range(len(array) + 1):
        if i == len(array) or array[i] == ' ':
            print(start_index, i-1)
            reverse(array, start_index, i-1)
            start_index = i + 1

    return array


test_1 = ['c', 'a', 'k', 'e', ' ',
          'p', 'o', 'u', 'n', 'd', ' ',
          's', 't', 'e', 'a', 'l']
print(solution(test_1) == ['s', 't', 'e', 'a', 'l', ' ',
                           'p', 'o', 'u', 'n', 'd', ' ', 'c', 'a', 'k', 'e'])
