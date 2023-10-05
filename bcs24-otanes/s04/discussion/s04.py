rows = 5

array_2d = [['Student No.', 'Student Name','Quiz 1', 'Quiz 2', 'Quiz 3', 'Quiz Total', 'Class Part.', 'Exam', 'Grade', 'Remarks']]

'''
 0           1               2   3   4   5   6   7     8        9
|Student No.|Student Name   |q1 |q2 |q3 |qT |cp |exam |grade   |remarks   |

0          1            2   3   4   5   6
102030400, Bob Waffles, 89, 78, 99, 69, 78
102430480, Mark Pancakes, 60, 60, 60, 60, 60
172031450, Jerry Cereals, 75, 78, 60, 69, 50
132730409, Maxx Noodles, 86, 78, 60, 69, 60
102131401, Kaff Bread, 60, 78, 60, 69, 78
'''

print("Example Input: 102030400, Bob Waffles, 89, 78, 99, 69, 78")
for i in range(rows):
    row_input = input(f"Enter Student {i + 1} Information: ")
    row_values = row_input.split(',')
    row_values = [item.strip() for item in row_values]
    
    quiz_total = (int(row_values[2])+ int(row_values[3]) + int(row_values[4]))/3
    grade = (int(row_values[5])*.1) + (quiz_total*.4) + (int(row_values[6])*.5)
    if grade >= 75:
        remark = "Passed"
    else:
        remark = "Failed"

    row_values.insert(5, f"{quiz_total:.2f}")
    row_values.insert(8, f"{grade:.2f}")
    row_values.insert(9, remark)

    array_2d.append(row_values)

for row in array_2d:
    print("|{:<12}|{:<20}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|{:<12}|".format(*row))
