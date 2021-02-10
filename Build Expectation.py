def find_substring(string, sub_string):
    l1 = len(string)
    l2 = len(sub_string)
    for i in range(l2-l1+1):
        for j in range(l1):
            if string[j] != sub_string[i+j]:
                break
            if j + 1 == l1:
                return 1
    return 0


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    print(find_substring(string, sub_string))
