def array_manipulation(n, queries):
    print(queries)
    start_array = []
    max = 0
    for i in range(n):
        start_array.append(0)

    temp = {}
    print(n)
    for i in range(len(queries)):
        for j in range(3):
            temp[queries[i][2]] = 0


if __name__ == "__main__":
    queries = []
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    print(array_manipulation(n, queries))
