def setGo(targetSum, numbers):
    T = []
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = setGo(remainder, numbers)
        if remainderResult != None:
            # Spread operator in Python
            T = [*remainderResult, num]
            return T
    return None


print(setGo(7, [2, 3]))
