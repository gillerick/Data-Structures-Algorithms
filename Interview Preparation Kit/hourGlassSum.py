def hour_glass_sum(m):
    best = sum(m[0][0:3]) + m[1][1] + sum(m[2][0:3])
    for i in range(4):
        for j in range(4):
            s = sum_glass(m, i, j)
            if s > best:
                best = s
    return best


def sum_glass(m, i, j):
    return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])


if __name__ == "__main__":
    m = [[1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(hour_glass_sum(m))
