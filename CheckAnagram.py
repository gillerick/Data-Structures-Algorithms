def IsAnagram(str1: str, str2: str):
    copyOfStr1 = str1.replace(" ", "")
    copyOfStr2 = str2.replace(" ", "")

    if len(copyOfStr1) != len(copyOfStr2):
        return False

    array_str1 = sorted(list(copyOfStr1.lower()))
    array_str2 = sorted(list(copyOfStr2.lower()))

    if array_str1 == array_str2:
        return True
    return False


if __name__ == "__main__":
    print(IsAnagram("listen", "Silent"))
