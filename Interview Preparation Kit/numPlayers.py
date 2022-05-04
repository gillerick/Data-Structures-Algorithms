def numPlayers(k, scores):
    scores_count = {}
    players_count = 0
    for score in sorted(scores, reverse=True):
        scores_count[score] = scores.count(score)
    for count in scores_count.values():
        while players_count < k:
            players_count += count
    return players_count


if __name__ == "__main__":
    print(numPlayers(4, [20, 40, 60, 80, 100]))
    print(numPlayers(1, [1, 3, 2, 1, 3, 2, 1]))
    print(numPlayers(4, [100, 50, 50, 25]))
    print(numPlayers(4, [2, 2, 3, 4, 5]))
    print(numPlayers(1, [1, 1, 2, 2, 3, 3]))
