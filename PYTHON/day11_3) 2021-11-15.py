# (1) 테스트용 샘플 DB 생성
'''
-- 데이타베이스 생성
CREATE DATABASE testdb1;
SHOW DATABASES;
'''

# (2) 테이블 생성
'''
-- testdb1 접속
-- bookTbl 테이블 생성
-- id, title, writer, page, price
USE testdb1;
CREATE TABLE bookTbl (
	id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title TEXT NOT NULL,
    writer VARCHAR(20) NOT NULL,
    page INTEGER NOT NULL,
    price INTEGER  NOT NULL
);
DESC bookTbl;
'''
# 데이터베이스 접속 및 커서 생성
import pymysql
import pandas as pd
import os

# DB 연결
conn = pymysql.connect( host = 'localhost',
                        port=3306, # mysql 포트
                        user='root', # 접속 계정
                        password = 'wjdwl7468!', # 루트계정의 본인 비번
                        db = 'testdb',  # 접속하고자 하는 데이타베이스명
                        charset = 'utf8' )
cursor = conn.cursor()
print(cursor)


# (3) 레코드 삽입
# 레코드 삽입 1
# 필드값이 auto_increment 인 경우 Null 값으로 지정
'''
sql = INSERT INTO 테이블명
        VALUES (값1, 값2,...)
cursor.execute(sql)
conn.commit()
'''
# sql = '''INSERT INTO bookTbl VALUES (NULL, "파이썬 완전정복", " 박파이", 600, 30000)'''
# cursor.execute(sql)
# 데이터베이스 반영
# conn.commit()


# 레코드 삽입 2 - % 사용
'''
sql = INSERT INTO 테이블명 VALUES (%s, %s...)
cursor.execute(sql, (값1, 값2...))
conn.commit()
'''

# sql = '''INSERT INTO bookTbl (title, writer, page, price) VALUES (%s, %s, %s, %s) '''
# cursor.execute(sql, ('이것이 MySQL이다', '박디비', 500, 35000))
# cursor.execute(sql, ('이것이 오라클이다', '박디비', 500, 23000))
# cursor.execute(sql, ('이것이 파이썬이다', '윤파이', 540, 33500))
# conn.commit()

# 레코드 삽입 3 - % 사용
'''
sql = INSERT INTO 테이블명 VALUES (%s, %s...)
cursor.execute(sql, 2차원 튜플)
conn.commit()
'''

# sql = '''INSERT INTO bookTbl (title, writer, page, price) VALUES (%s, %s, %s, %s)'''
# 2차원 튜플 형태로 삽입 레코드 정의
# data = (('혼공 머시러닝','김머신', 800, 70000),
        # ('데이터분석 완전정복', '김데이터', 800, 6000),
        # ('머시러닝 핸드북','송머신', 500, 55000))
# cursor.executemany(sql, data)
# conn.commit()


# (4) 레코드 삭제
'''
sql ="DELETE FROM 테이블명 WHERE 필드 = %s"
cursor.execute(sql, (값1,))
conn.commit()
'''
# sql ="DELETE FROM bookTbl WHERE id = %s"
# cursor.execute(sql, (1,))
# conn.commit()


# (5) 레코드 수정
'''
sql = "UPDATE 테이블명 SET 필드1 = %s WHERE 필드2 = %s"
cursor.execute(sql, (값1,값2....))
conn.commit()
'''

sql = "UPDATE bookTbl SET price = %s WHERE id = %s"
cursor.execute(sql, (15000, 2))
conn.commit()


