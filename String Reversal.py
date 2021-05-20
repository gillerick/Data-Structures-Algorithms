def reverseString(string):
    reversedStr = ""
    count = len(string) - 1
    for i in range(0, len(string)):
        while count >= 0:
            reversedStr += string[count]
            count -= 1
        return reversedStr


if __name__ == "__main__":
    print(reverseString("Hey there, how are you doing"))


