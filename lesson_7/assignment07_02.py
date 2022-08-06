# Згенерувати, за допомогою list comprehension,
# квадратну диагональну матрицю завданої розмірності (N)
# N - запитати у користувача
#
# Приклад:
# N = 4
#
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
# підказка: j+1 if i = j else 0
#
from doctest import OutputChecker


N = int(input('Enter a positive number: '))

a = [[j + 1 if j == i else 0 for i in range(N)] for j in range(N)]

# 1
for row in a:
    print(row)

# 2 
for i in range(N):
    for j in range(N):
        if i == j:
            j += 1
        else:
            j = 0
        print(j, end='')    
    print()

# output:
# Enter a positive number: 5

# [1, 0, 0, 0, 0]
# [0, 2, 0, 0, 0]
# [0, 0, 3, 0, 0]
# [0, 0, 0, 4, 0]
# [0, 0, 0, 0, 5]

# 10000
# 02000
# 00300
# 00040
# 00005