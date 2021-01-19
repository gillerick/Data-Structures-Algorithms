def merge_the_tools(string, k):
    arr = [*(n for n in range(0, len(string)) if n % k == 0), len(string)]
    for i in range(len(arr)):
        try:
            new_tool = ""
            tool = str(string[arr[i]:arr[i+1]])
            for c in tool:
                if c not in new_tool:
                    new_tool += c
            print(new_tool)
        except IndexError:
            pass


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
