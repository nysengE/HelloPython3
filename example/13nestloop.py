#중첩 반복문
#2개 이상의 반복문을 이용해서 반복실행할 수도 있음
#하나의 반복문 안에 다른 반복문을 포함시킨 것을 의미
#2차원 배열처리나, 달력 출력 등 복잡한 패턴 구현가능

# *
# **
# ***
# ****
# *****
for i in range(1, 5 + 1):
    for j in range(i):
        print('*', end='')
    print()
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

#구구단 출력
for i in range(2, 9 + 1):
    for j in range(2, 9 + 1):
        print(f'{j} x {i} = {i * j:02d}   ', end='')
    print()
#구구단(19) 출력
for i in range(1, 19 + 1):
    for j in range(2, 19 + 1):
        print(f'{j:02d} x {i:02d} = {i * j:03d}   ', end='')
    print()
#2차원배열
for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        print(f'''          Multiplication Table
        ''')
    print()