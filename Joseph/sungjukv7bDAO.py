import sqlite3

# 성적 데이터 총 갯수 조회
def getTotalSungJuk():
    sql = 'select count(sjno) + 1 total from sungjuk'
    cnt = 0
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    for r in rs:
        cnt = r[0]
    cursor.close()
    conn.close()
    return cnt

# 처리된 성적데이터를 테이블에 저장
def newSungJuk(sj):
    sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) \
           values (?,?,?,?, ?,?,?)'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sj[1],sj[2],sj[3],sj[4],sj[5],sj[6],sj[7])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터 추가됨!')
    conn.commit()
    cursor.close()
    conn.close()

# 성적 데이터 전체 조회
def readAllSungJuk():
    sql = 'select sjno,name,kor,eng,mat,substr(regdate,0,11) regdate from sungjuk'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    sjs = cursor.fetchall()
    cursor.close()
    conn.close()
    return sjs

# 학생 한명의 성적 상세 조회
def readOneSungJuk(sjno):
    sql = 'select * from sungjuk where sjno = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sjno,)
    cursor.execute(sql, params)
    sj = cursor.fetchone()
    cursor.close()
    conn.close()
    return sj

# 학생 데이터 삭제
def delDataSungJuk(sjno):
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    sql = 'delete from sungjuk where sjno = ?'
    params = (sjno,)
    cursor.execute(sql, params)
    del_count = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return del_count

def updateSungJuk(sj):
    sql = 'update sungjuk set kor=?, eng=?, mat=?, tot=?, avg=?, grd=? where sjno =?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sj[2],sj[3],sj[4],sj[5],sj[6],sj[7],sj[0])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터 수정됨!')
    conn.commit()
    cursor.close()
    conn.close()
    return sj