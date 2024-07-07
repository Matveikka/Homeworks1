grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students1 = sorted(students)
listok = []
for x in grades:
    grade = sum(x)/len(x)
    listok.append(grade)
dictionary = dict(zip(students1, listok))
print(dictionary)










