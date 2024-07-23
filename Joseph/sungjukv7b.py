import Joseph.sungjukv7bDAO as sjv7dao

def displayMenu():
    main_menu = '''
    =========================
        성적 프로그램 v7b
    =========================
       1. 성적 데이터 추가
       2. 성적 데이터 조회
       3. 성적 데이터 상세조회
       4. 성적 데이터 수정
       5. 성적 데이터 삭제
       0. 성적 프로그램 종료
    ========================= 
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

# 성적 데이터를 입력 받는 함수
def readSungJuk():
    sj = []
    cnt = sjv7dao.getTotalSungJuk()
    sj.append(cnt)
    sj.append(input(f'추가할 학생 이름은? '))
    sj.append(int(input(f'추가할 학생의 국어 점수는? ')))
    sj.append(int(input(f'추가할 학생의 영어 점수는? ')))
    sj.append(int(input(f'추가할 학생의 수학 점수는? ')))
    return sj

# 입력받은 성적 데이터를 처리하고 테이블에 저장
def addSungJuk(sj):
    computeSungJuk(sj)
    sjv7dao.newSungJuk(sj)

# 테이블에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    sjs = sjv7dao.readAllSungJuk()
    for sj in sjs:
        result += f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}, 등록일: {sj[5]}\n'
    print(result)

# 학생 번호로 성적데이터 조회후 출력
def showOneSungJuk():
    # name = input('조회할 학생 이름은? ')
    sjno = input('조회할 학생의 번호는? ')
    result = '데이터가 존재하지 않아요!!'
    sj = sjv7dao.readOneSungJuk(sjno)
    if sj:   # 조회한 데이터가 존재한다면
        result = (f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}\n'
                  f'총점: {sj[5]}, 평균: {sj[6]:.1f}, 학점: {sj[7]}, 등록일: {sj[8]}')
    print(result)

# 입력한 성적데이터에 대해 성적처리하는 함수
def computeSungJuk(sj):
    sj.append(sj[2] + sj[3] + sj[4])
    sj.append(sj[5] / 3)
    grd = '수' if (sj[6] >= 90) else \
        '우' if (sj[6] >= 80) else \
            '미' if (sj[6] >= 70) else \
                '양' if (sj[6] >= 60) else '가'
    sj.append(grd)

# 학생번호를 입력받아 데이터 삭제
def delSungJuk():
    sjno = input('삭제할 학생의 번호는? ')
    del_count = sjv7dao.delDataSungJuk(sjno)
    if del_count > 0:   # 조회한 데이터가 존재한다면
        print(f'{del_count} 건의 데이터가 삭제됨!')
    else:
        print('데이터가 존재하지 않아요!!')

def modifySungJuk():
    sjno = input('수정할 학생의 번호는? ')
    result = '데이터가 존재하지 않아요!!'
    sj = sjv7dao.readOneSungJuk(sjno)
    if sj:   # 조회한 데이터가 존재한다면
        nsj = readAgainSungJuk(sj)
        sj = sjv7dao.updateSungJuk(nsj)  # 수정된 데이터를 반환받음
        result = (f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}\n'
                  f'총점: {sj[5]}, 평균: {sj[6]:.1f}, 학점: {sj[7]}')
    print(result)

# 기존 성적 데이터를 확인하면서 수정할 성적 데이터 재입력
def readAgainSungJuk(sj):
    nsj = []
    nsj.append(sj[0])
    nsj.append(sj[1])
    nsj.append(int(input(f'수정할 국어 점수는? ({sj[2]}) ')))
    nsj.append(int(input(f'수정할 영어 점수는? ({sj[3]}) ')))
    nsj.append(int(input(f'수정할 수학 점수는? ({sj[4]}) ')))
    computeSungJuk(nsj)
    return nsj
