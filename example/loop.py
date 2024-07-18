#1~100사이 정수 중 3과 8의 최소공배수 수하기
result = ''

for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 8 == 0:
        result += f'{i} '
print(result, f'[{3 * 8}]')

#삼각형 넓이 구하기
limit = 150
width = 2
height = 3
i = 1

while True:
    area = ((width * i) * (height * i)) / 2
    if area > limit: break
    print(f'삼각형 너비 : {width * i} / {height * i} = {area}')
    i += 1

#로그인 기능 만들기
cutlogin = 0
while True:
    passwd = input('관리자 암호를 입력하세요 : ')

    if passwd == 'passwd':
        print('로그인 되었습니다.')
        break
    else:
        print('암호를 다시 입력해주세요.')

    if cutlogin < 5:
        cutlogin += 1
        print(f'로그인 시도 회수 {cutlogin} / 5')
    else:
        print('로그인 시도 횟수 초과')
        break

#반복문내 건너뛰기 : continue
#for, while문 내에서 반복 흐름을 일시적으로 넘기기 위해 사용

#1~10 사이 정수 중 홀수의 합 출력
sum = 0

for i in range(1, 10 + 1):
    if i % 2 == 0: continue
    sum += i

print(sum)

#1~100 사이 정수의 합을 출력
#3의 배수나 7의 배수는 제외
sum = 0

for i in range(1, 100 + 1):
    if i % 3 == 0 or i % 7 == 0: continue
    sum += i

print(sum)
#-----------------------------------------
sum = 0
i = 1

while i <= 100:
    if i % 3 == 0 or i % 7 == 0:
        i += 1
        continue
    sum += i
    i += 1

print(sum)
#-----------------------------------------
sum = 0
i = 0

while i < 100:
    i += 1
    if i % 3 == 0 or i % 7 == 0: continue
    sum += i

print(sum)