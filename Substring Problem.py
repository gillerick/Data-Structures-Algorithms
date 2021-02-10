def find_infString(string, infString):
    l1 = len(string)
    l2 = len(infString)

    if l2 % l1 != 0:
        return False
    if l2 == l1 and string == infString:
        return True
    for i in range(l1, l2):
        if infString[l1:] != string:
            return False
        return True


print(find_infString("abcd", "abcdth"))
