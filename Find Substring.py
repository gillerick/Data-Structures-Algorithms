def count_substring(string, sub_string):
    l1 = len(sub_string)
    l2 = len(string)
    count = 0
    for i in range(l2-l1+1):
        for j in range(l1):
            if sub_string[j] != string[i+j]:
                break
            if j + 1 == l1:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
