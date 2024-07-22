import os
import sqlite3

# 데이터베이스 경로
db_path = 'db/python.db'
db_dir = os.path.dirname(db_path)

# 디렉토리가 없으면 생성
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# 데이터베이스 연결
conn = sqlite3.connect(db_path)

# 데이터베이스 커서 생성
cursor = conn.cursor()

# 테이블 생성 SQL 작성
sql = '''
CREATE TABLE member (
    userid VARCHAR(18) NOT NULL,
    passwd VARCHAR(18) NOT NULL,
    name VARCHAR(18) NOT NULL,
    email VARCHAR(35) NOT NULL
)
'''

# SQL 실행
cursor.execute(sql)
conn.commit()

# 작업 마무리
cursor.close()
conn.close()

# -------------------------------------------------------------------------------------------------

# 파이썬으로 데이터베이스 다루기 2 - 데이터 추가
import sqlite3

userid = input('아이디는? ')
passwd = input('비밀번호는? ')
name = input('이름은? ')
email = input('이메일은? ')

# 1
conn = sqlite3.connect('db/python.db')

# 2
cursor = conn.cursor()

# 3

# sql = f'''
# insert into member
# values ('{userid}', '{passwd}', '{name}', '{email}')
# '''
# ㄴ> SQL injection 공격 위험 존재

# 매개변수 placeholer(?)를 이용해서 실제 값을 대입
sql = 'insert into member values (?, ?, ?, ?)'
params = (userid, passwd, name, email)

# 4
# cursor.execute(sql)
cursor.execute(sql, params)
print(cursor.rowcount, '건의 데이터가 추가됨!')
conn.commit()
# 5
cursor.close()
conn.close()

# -------------------------------------------------------------------------------------------------

# 파이썬으로 데이터베이스 다루기 3 - 데이터 조회

# 1
conn = sqlite3.connect('db/python.db')

# 2
cursor = conn.cursor()

# 3
sql = 'select * from member'

# 4 - sql을 실행하고 결과 집합을 가져옴
cursor.execute(sql)
rs = cursor.fetchall()

# 5 - 결과 집합에서 레코드 단위로 읽어와서 회원정보 출력
result = ''
for r in rs:
    result += f'{r[0]} {r[1]} {r[2]} {r[3]}\n'
print(result)

# 6
cursor.close()
conn.close()

# 파이썬으로 데이터베이스 다루기 4 - 데이터 수정

# 파이썬으로 데이터베이스 다루기 5 - 데이터 상세 조회
# 1
conn = sqlite3.connect('db/python.db')

# 2
cursor = conn.cursor()

# 3
sql = 'select * from member where userid = ?'
params = ('id1',)

# 4
cursor.execute(sql, params)
# rs = cursor.fetchone() -> 결과가 한 개만 존재 할 때
rs = cursor.fetchone()

# 5
print(f'{rs[0]},{rs[1]},{rs[2]},{rs[3]}')

# 6
cursor.close()
conn.close()


# 파이썬으로 데이터베이스 다루기 6 - 데이터 삭제
# 1
conn = sqlite3.connect('db/python.db')

# 2
cursor = conn.cursor()

# 3
sql = 'delete from member where userid = ?'
params = ('11',)

# 4
cursor.execute(sql, params)
print(cursor.rowcount, '건의 데이터가 삭제됨!')
conn.commit()

# 5
cursor.close()
conn.close()
