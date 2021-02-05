def find_sub(string, substring):
    l1 = len(string)
    l2 = len(substring)

    if substring == [] and string == []:
        return True
    if l2 == l1 and string == substring:
        return True
    # if l2 < l1 and string[:l2] == substring:
    #     return True

    for i in range(l1, l2):
        if str(substring).index(str(string)) == 0:
            substring = substring[:l1]
            if find_sub(string, substring):
                return True

    return False


print(find_sub('abcd', 'abcdabcdabu'))
