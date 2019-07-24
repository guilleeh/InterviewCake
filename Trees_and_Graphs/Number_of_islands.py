class Solution:
    def __init__(self):
        self.dir_row = [0, -1, 0, 1]  # left, up, right, down
        self.dir_col = [-1, 0, 1, 0]  # ^^

    def dfs(self, grid: [[int]], row, col):
        # sink current one
        grid[row][col] = 0
        for d in range(4):
            # Check all 4 directions
            new_row = row + self.dir_row[d]
            new_col = col + self.dir_col[d]
            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                if grid[new_row][new_col]:
                    self.dfs(grid, new_row, new_col)

    def number_of_islands(self, grid: [[int]]) -> int:
        total_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    self.dfs(grid, row, col)
                    total_islands += 1

        return total_islands


if __name__ == "__main__":
    input_1 = [[1, 1, 1, 1, 0],
               [1, 1, 0, 1, 0],
               [1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    input_2 = [[1, 1, 0, 0, 0],
               [1, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 1]]

    solution = Solution()
    print(solution.number_of_islands(input_1))
    print(solution.number_of_islands(input_2))
