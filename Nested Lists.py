'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
Example:
The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:
'''

A = []
if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = float(input())
        # Appending the inputs as sub-list (nested list)
        A.append([name, score])
    # Sorting and removing duplicates from the list
    S = sorted(set([x[1] for x in A]))
    if len(S) > 1:
        for name in sorted(x[0] for x in A if x[1] == S[1]):
            print(name)
