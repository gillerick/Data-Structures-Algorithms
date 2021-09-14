# Design an alogrithm to find all pairs of integers within an array which sum to a specified value
# Optimized solution

def sum_pairs(array, sum:int):
    array_pairs = []
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == sum:
                array_pairs.append(array[i])
                array_pairs.append(array[j])
    array_pairs = set(array_pairs)
    return array_pairs


if __name__ == "__main__":
    array = [5, 6, 7, 2, 1, 5]
    print(sum_pairs(array, 6))
