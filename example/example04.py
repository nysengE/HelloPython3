#27 - 윤년 구분 isLeapYear
def isLeapyear(year):
    isLeap = '윤년 아님!'

    cond1 = (year % 4 == 0) and (year % 100 != 0)
    cond2 = (year % 400 == 0)
    if cond1 or cond2: isLeap = '윤년 입니다.'

    print(f'{year} 년은 {isLeap}')