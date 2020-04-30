number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

alphanum_grid = [
    [1, 2, 3],
    ["A", "B", 6],
    ["C", 8, "E"],
    ["F, G, H"]
]
print(number_grid)
print(number_grid[0])
print(number_grid[0:])
print(number_grid[0][1])
print(number_grid[2][1])

print(alphanum_grid)
print(alphanum_grid[2][0])
print(alphanum_grid[3][0])

print("--For Loop--")

for row in number_grid:
    print(row)

print("--Nested For Loop--")

for row in number_grid:
    for col in row:
        print(col)