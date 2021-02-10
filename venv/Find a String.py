import sys

def getInput():
    raw_input = list(map(str, input("Enter string and substring").split(" ")))
    # raw_input = sys.stdin.readlines()
    form_input = [s[:s.find(' ')] if ' ' in s else s for s in raw_input]
    return form_input

def occurences(s, sub):
    return len([n for n in range(len(s)) if s.find(sub, n) == n])

inp = getInput()
print(occurences(inp[0], inp[1]))