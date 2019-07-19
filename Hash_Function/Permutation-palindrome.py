from collections import defaultdict


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    string_length = len(the_string)
    character_counts = defaultdict(int)
    for char in the_string:
        character_counts[char] += 1

    if string_length % 2 == 0:
        for key, value in character_counts.items():
            if value % 2 != 0:
                return False
        return True
    else:
        odd_count = 0
        for key, value in character_counts.items():
            if value % 2 == 1:
                odd_count += 1

        return odd_count == 1


print(has_palindrome_permutation('aabccbdd') == True)
print(has_palindrome_permutation('aabcbcd') == True)

print(has_palindrome_permutation('aabcd') == False)
print(has_palindrome_permutation('aabbcd') == False)

print(has_palindrome_permutation('') == True)
print(has_palindrome_permutation('a') == True)
