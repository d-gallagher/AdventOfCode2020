from rich.traceback import install
from rich import print
install()


def get_grid(file):
    with open(file, "r") as f:
        grid = [[i for i in _] for _ in f.read().splitlines()]
    return grid

def move(grid, steps):
    x = trees = 0

    # Move y steps
    for y in range(0, len(grid), steps[1]):
        # wrap around the row
        x = x % len(grid[0])
        # sum trees
        trees += 1 if g[y][x] == "#" else 0
        # move x steps
        x += steps[0]
    print("Trees: ", trees)
    return trees

g = get_grid("Day3/input.txt")
tuples = [(1,1),(3,1),(5,1),(7,1),(1,2)]
# print(tuples[1][1])
result = 1
for t in tuples:
    result *= move(g, t)


print(f'Result: {result}')
