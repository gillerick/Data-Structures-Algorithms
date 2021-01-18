"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format:

The first line contains the integer , the number of students' records.
The next  lines contain the names and marks obtained by a student, each value separated by a space.
The final line contains query_name, the name of a student to query.
"""

if __name__ == "__main__":
    students_dict = {}
    n = int(input())
    for i in range(n):
        student_details = input().split()
        students_dict[student_details[0]] = sum(map(float, student_details[1:])) / 3.0
    query = input()
    print(students_dict[query])


"""
Alternative solution

N = int(raw_input())
dictionary = {}
for _ in range(N):
    A = raw_input().split()
    name = A.pop(0)
    dictionary[name] = map(float, A)
name = raw_input()
print "{0:.2f}".format(1.00*sum(dictionary[name])/len(dictionary[name]))

"""
