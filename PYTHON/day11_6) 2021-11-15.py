# csv => 데이터프레임 => MYSQL에 등록된 테이블에 레코드로 삽입
# 데이터베이스 접속 및 커서 생성
import pymysql
import pandas as pd
import os
import sqlalchemy


# DB 연결
conn = pymysql.connect( host = 'localhost',
                        port=3306, # mysql 포트
                        user='root', # 접속 계정
                        password = 'wjdwl7468!', # 루트계정의 본인 비번
                        db = 'testdb',  # 접속하고자 하는 데이타베이스명
                        charset = 'utf8' )
cursor = conn.cursor()
print(cursor)

# (1) csv => 데이터프레임
df = pd.read_csv('data/population.csv')
print(df.shape)  #(51, 2)

# 데이터프레임의 필드 정보 확인
print(df.info())

# (2) DB 정보 => 엔진 객체에 등록
# sqlalchemy 엔진 정보 생성
# url = 'mysql+pymysql://아이디:패스워드@localhost:3306/데이타베이스명'
url = 'mysql+pymysql://root:wjdwl7468!@localhost:3306/testdb'
engine = sqlalchemy.create_engine(url)
print(engine)

# (3) to_sql()로 데이터베이스의 테이블로 등록
df.to_sql(name='population2', con=engine, if_exists='append', index=True)

conn.close()

# (4) 워크벤치에서 확인
'''
SHOW TABLES;
SELECT * FROM population2;
DESC population2;
'''

