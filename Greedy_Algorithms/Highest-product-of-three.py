def get_first_three_order(sub_list_of_ints: list) -> tuple:
    first = max(sub_list_of_ints)
    sub_list_of_ints.remove(first)
    second = max(sub_list_of_ints)
    sub_list_of_ints.remove(second)
    third = sub_list_of_ints[0]
    return (first, second, third)


def highest_product_of_three(list_of_ints: list) -> int:
    first, second, third = get_first_three_order(list_of_ints[:3])
    current_max = first * second * third

    for number in list_of_ints[3:]:
        if number > first:
            second, third = first, second
            first = number
        elif number > second:
            third = second
            second = number
        else:
            third = number

        if first * second * third > current_max:
            current_max = first * second * third

    return current_max


test_1 = [1, 2, 3]
test_2 = [0, 1, 0]
test_3 = [3, 7, 4, 1, 6, 5]
test_4 = [1, 2, 3, 4]
test_5 = [6, 1, 3, 5, 7, 8, 2]
test_6 = [-5, 4, 8, 2, 3]
test_7 = [-10, 1, 3, 2, -10]

print(highest_product_of_three(test_1) == 6)
print(highest_product_of_three(test_2) == 0)
print(highest_product_of_three(test_3) == 210)
print(highest_product_of_three(test_4) == 24)
print(highest_product_of_three(test_5) == 336)
print(highest_product_of_three(test_6) == 96)
print(highest_product_of_three(test_7) == 300)
