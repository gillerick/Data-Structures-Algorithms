def numPlayers(k, scores):
    array_set = set(scores)
    if len(array_set) > k:
        return k
    return len(array_set)


if __name__ == "__main__":
    print(numPlayers(4, [20, 40, 60, 80, 100]))
    print(numPlayers(4, [100, 50, 50, 25]))
    print(numPlayers(4, [2, 2, 3, 4, 5]))
