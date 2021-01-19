def merge_the_tools(string, k):
    memo = {}
    arr = [*(n for n in range(0, len(string)) if n % k == 0), len(string)]
    for i in range(len(arr)):
        try:
            tool = [str(string[arr[i]:arr[i+1]])]
            for j, k in zip(tool, range(1, len(tool))):
                if j == tool[k+1]:
                    tool.remove(j)
                print(tool)
        except IndexError:
            pass


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
