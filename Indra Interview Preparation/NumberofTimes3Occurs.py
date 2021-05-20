def count_3s(n):
    count = 0
    while n > 0:
        if n % 10 == 3:
            count += 1
        n = int(n / 10)
    return count


def count_in_range(n):
    count = 0
    for i in range(2, n):
        count += count_3s(i)
    return count


if __name__ == "__main__":
    number = int(input("Enter the number\n"))
    print(count_in_range(number))
