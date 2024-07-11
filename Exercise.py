#매출액 입력 시 총합 출력
month1 = int(input('1월 매출액을 입력 하세요 : '))
month2 = int(input('2월 매출액을 입력 하세요 : '))
month3 = int(input('3월 매출액을 입력 하세요 : '))
print(f'''
1월 매출액 : {month1}
2월 매출액 : {month2}
3월 매출액 : {month3}
1분기 전체 매출 : {month1 + month2 + month3} 원
''')

#1분기 수익 계산
sale = int(input('1분기 매출을 입력 하세요 : '))
buy = int(input('1분기 매입을 입력 하세요 : '))
print(f'''
1분기 매출액 : {sale}
1분기 매입액 : {buy}
수익 : {sale - buy} 원
''')

#방의 넓이 구하기
width = int(input('방의 가로 길이를 입력 하세요 : '))
length = int(input('방의 세로 길이를 입력 하세요 : '))
print(f'''
가로 길이 : {width}
세로 길이 : {length}
방의 넓이 : {width * length} ㎠
''')

#신체질량지수 구하기
w = int(input('몸무게를 입력 하세요 : '))
t = int(input('신장을 입력 하세요 : '))
print(f'''
몸무게(kg) : {w}
신장(cm) : {t}
BMI 지수 : {int(w / (t / 100)**2)}
''')

#홀짝게임
game = int(input('손 안에 동전 수를 입력 하세요 : '))
print(game % 2)

#빵 나누기
brad = int(input('빵의 총 개수를 입력 하세요 : '))
total = int(input('한 명당 나누어줄 빵의 개수를 입력 하세요 : '))
print(f'''
빵을 나누어 줄 수 있는 학생 수 : {brad // total}
남은 빵의 개수 : {brad % total}
''')

#전염병 예상 감염자 구하기
print('전염병 확산 추세')
day = int(input('날짜를 입력 하세요 : '))
print(f'''
{day}일 이후 감염자 수 :  {2 ** day} 
''')


#성적 처리 프로그램 v1
#이름, 국어, 영어, 수학을 입력 받으면 총점, 평균, 학점을 계산하고 출력함
#학점은 수우미양가로 표현
#이름: 홍길동, 국어: 99, 영어: 98, 수학: 99, 총점: 296, 평균: 98.6, 학점: 수

name = input('이름을 입력하세요 : ')
ko = int(input('국어 점수를 입력하세요 : '))
en = int(input('영어 점수를 입력하세요 : '))
ma = int(input('수학 점수를 입력하세요 : '))

total = ko + en + ma
avg = total / 3

hak = ""
if avg >= 90:
    hak = "수"
elif avg >= 80:
    hak = "우"
elif avg >= 70:
    hak = "미"
elif avg >= 60:
    hak = "양"
else:
    hak = "가"

print(f'''
{name} 학생
국어 점수 {ko}점, 영어 점수 {en}점, 수학 점수 {ma}점

총점은 {total}입니다.
평균 점수는 {avg:.1f}입니다.
학점은 {hak}입니다.
''')