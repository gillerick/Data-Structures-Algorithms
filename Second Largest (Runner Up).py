def runner_up(A):
    return sorted(set(A))[-2]


if __name__ == "__main__":
    test = int(input())
    # A = [int(_) for _ in input().split(',')]
    A = map(int, input().split(','))
    print(runner_up(A))
