def jumping_on_clouds(c):
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 1 if c[1] == 0 else 1
    if c[2] == 1:
        return 1 + jumping_on_clouds(c[1:])
    if c[2] == 0:
        return 1 + jumping_on_clouds(c[2:])


if __name__ == "__main__":
    c = [0, 1, 0, 0, 0, 1, 0]
    print(jumping_on_clouds(c))
