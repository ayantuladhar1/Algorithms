# Name: Ayan Tuladhar

# The following program uses DP implementation to calculate Optimal Binary Search Tree cost.


MAXIMUM = 2147483647
def OBST(root, number, n):
    how_much = [[0 for x in range(n)]
            for y in range(n)]
    for a in range(n):
        how_much[a][a] = number[a]
    for b in range(2, n + 1):
        for x in range(n - b + 2):
            y = x + b - 1
            if x >= n or y >= n:
                break
            how_much[x][y] = MAXIMUM
            for z in range(x, y + 1):
                c = 0
                if z > x:
                    c += how_much[x][z - 1]
                if z < y:
                    c += how_much[z + 1][y]
                c += add(number, x, y)
                if c < how_much[x][y]:
                    how_much[x][y] = c
    return how_much[0][n - 1]


def add(number, a, b):
    p = 0
    for k in range(a, b + 1):
        p += number[k]
    return p


if __name__ == '__main__':
    root = [100, 200, 300]
    number = [10, 20, 30]
    n = len(root)
    print("how_much of Optimal BST is",
          OBST(root, number, n))