# ----------------------------------------
#У Петрика є два числа a та b (a≤b).
# Він знайшов середнє арифметичне цих чисел (нехай, це буде число c), яке виявилось теж цілим.
# Тобто, c= (a+b)/2
# Вам дано число a (тобто менше з тих двох чисел), а також дано число c. Знайдіть b.

# Приклади
# Вхідні дані #1
# 37
# Відповідь #1
# 11
numRows = int(input())
answer = []

for i in range(numRows):
    grid = []
    for j in range(i+1):
        if j == 0 or j == i:
            grid.append(1)
            continue
        x = answer[i-1][j-1] + answer[i-1][j]
        grid.append(x)
    answer.append(grid)

for i in range(numRows):
    for j in range(i):
        print(answer[i][j])