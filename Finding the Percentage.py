"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format:

The first line contains the integer , the number of students' records.
The next  lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.
"""

if __name__ == "__main__":
    n = int(input("Enter the number of students\n"))
    for i in range(n):
        # Capturing student details. It is important to note that the resulting 'Results' is a list
        results = input().split(' ')
        # Storing captured data into a dictionary
        results_dict = {results[0]: [int(results[x]) for x in (range(1, len(results)))]}
    query = input("Enter the student name to query average:\n")
    print((results_dict[query][0] + results_dict[query][1] + results_dict[query][2])/3)


