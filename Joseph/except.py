# 프로그램 실행1
print('프로그램 실행 시작')
print('프로그램 실행 끝')

# 프로그램 실행2
print('프로그램 실행 시작')
print(10 / 0)
print('프로그램 실행 끝')

# 프로그램 실행3
print('프로그램 실행 시작')
t = [1, 2, 3]
print(t[100])
print('프로그램 실행 끝')

# 프로그램 실행4
print('프로그램 실행 시작')
try:
    print(10 / 0)
except:
    print('0으로 나눌 수는 없습니다.')
print('프로그램 실행 끝')

# 프로그램 실행5
print('프로그램 실행 시작')
t = [1, 2, 3]
try:
    print(t[100])
except:
    print('리스트 인덱스 초과.')
print('프로그램 실행 끝')

# 프로그램 실행6 - 예외처리가 포괄적임
n = [1, 10, 20, 50]

try:
    idx = int(input('n에서 사용할 값의 인덱스는?'))
    divr = int(input('선택한 값을 나눌 정수는?'))
    print(n[idx] / divr)
except:
    print('오류발생')
