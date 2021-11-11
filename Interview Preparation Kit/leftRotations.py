def left_rotate(a, d):
    len_arr = len(a)

    while d > len_arr:
        d -= len_arr

    first = list(map(str, a[d:]))
    last = list(map(str, a[:d]))
    return ' '.join(first + last)


if __name__ == "__main__":
    first_multiple_input = input().split()
    len_array = int(first_multiple_input[0])
    rotations = int(first_multiple_input[1])
    a = list(map(int, input().split()))[:len_array]
    print(left_rotate(a, rotations))
