# num = map(int, input().split())
# n1, n2 = num
# counter = 0
# for i in range(n1, n2 + 1):
#     i = str(i)
#     if i.count("5") == 0:
#         counter += 1
#
# print(counter)

#================================

#Picture: https://leetcode.com/problems/projection-area-of-3d-shapes/description/
 #
 # Вам дано сітку розміром n x n, де ми розміщуємо деякі кубики розміром 1 x 1 x 1, які вирівняні по осях x, y та z.
 # Кожне значення v = grid[i][j] представляє вежу з v кубиків, розміщених на клітинці (i, j).
 # Ми спостерігаємо проекцію цих кубиків на площини xy, yz та zx.
 # Проекція подібна до тіні, яка відображає нашу тривимірну фігуру на двовимірну площину.
 # Ми бачимо "тінь", коли дивимося на кубики зверху, спереду та збоку.
 # Поверніть загальну площу всіх трьох проекцій.
 #
 # Input: grid = [[1,2],[3,4]]
 # Output: 17
 # Explanation: Ось три проекції ("тіні") фігури, утвореної на кожній площині, вирівняній за осями.
 #
 # Example 2:
 # Input: grid = [[2]]
 # Output: 5
 #
 # Example 3:
 # Input: grid = [[1,0],[0,2]]
 # Output: 8


# grid = [[1,2],[3,4]]
# xy = 0
# yz = 0
# zx = 0
#
# for i in range(len(grid)):
#      for j in range(len(grid[i])):
#         xy += 1
#
#
#
# for i in range(len(grid)):
#     max2 = 0
#     for j in range(len(grid[i])):
#         if grid[i][j] > max2:
#             max2 = grid[i][j]
#     yz += max2
#
#
#
#
# for j in range(len(grid[0])):
#     max2 = 0
#     for i in range(len(grid)):
#         if grid[i][j] > max2:
#             max2 = grid[i][j]
#
#     zx += max2
#
#
#
# ans = xy + yz + zx
# print(ans)


# https://leetcode.com/problems/island-perimeter/description/
# Вам дано масив, який представляє карту землі і суші, де grid[i][j] = 1 означає сушу, а grid[i][j] = 0 означає воду.
# Клітинки сітки з'єднані горизонтально/вертикально (не по діагоналі). Сітка повністю оточена водою, і є рівно один острів
# (тобто одна або більше з'єднаних клітинок суші).
# Острів не має "озер", тобто вода всередині не з'єднана з водою навколо острова. Одна клітинка є квадратом зі стороною довжиною 1.
# Сітка прямокутна, ширина та висота не перевищують 100. Визначте периметр острова.
#
# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
# Example 2:
# Input: grid = [[1]]
# Output: 4
#
# Example 3:
# Input: grid = [[1,0]]
# Output: 4

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
P = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            if j == 0 or j == len(grid[i])-1:
                P += 1
            if  i == 0 or i == len(grid)-1:
                P += 1

            if j != 0:
                susid = grid[i][j-1]
                if susid != 1:
                    P += 1

            if j != len(grid[i]):
                susid = grid[i][j+1]
                if susid != 1:
                    P += 1
                    if j == len(grid[i]):
                        P += 1
            if i != 0:
                susid = grid[i-1][j]
                if susid != 1:
                    P += 1
                    if i == 0:
                        P += 1
            if i != len(grid)-1:
                susid = grid[i+1][j]
                if susid != 1:
                    P += 1
                    if i == len(grid)-1:
                        P += 1

print(P)



