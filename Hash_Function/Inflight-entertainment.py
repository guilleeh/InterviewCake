def solution(flight_length: int, movie_lengths: list):
    table = {}
    for movie in movie_lengths:
        if movie in table:
            return True
        table[flight_length - movie] = 1

    return False


print(solution(6, [2, 4]))
print(solution(6, [3, 8, 3]))
