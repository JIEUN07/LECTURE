# pymysql을 이용한 데이터베이스 연동
# 모듈 임포트
import pymysql
import pandas as pd
import os

conn = pymysql.connect( host = 'localhost',
                        port=3306, # mysql 포트
                        user='root', # 접속 계정
                        password = 'wjdwl7468!', # 루트계정의 본인 비번
                        db = 'world',  # 접속하고자 하는 데이타베이스명
                        charset = 'utf8' )

# 커서 생성
cursor = conn.cursor()
# <pymysql.cursors.Cursor object at 0x000001D308AB9490>
print(cursor)

#  (3) 접속 데이터베이스의 테이블정보 -> 파이썬 데이터
# 테이블 read
# sql = select 구문
# 데이터변수명 = cursor.fetchall(), cursor.fetchone(), cursor.fetchmany()

sql = 'select * from city limit 20';
cursor.execute(sql)
citydata = cursor.fetchall()  # 2차원 튜플
'''
citydata = cursor.fetchone()  # 1차원 튜플
citydata = cursor.fetchmany(3)  # 2차원 튜플
((1, 'Kabul', 'AFG', 'Kabol', 1780000), (2, 'Qandahar', 'AFG', 'Qandahar', 237500), (3, 'Herat', 'AFG', 'Herat', 186800))
'''
print(citydata)  
print(type(citydata))  # <class 'tuple'>
print(len(citydata))  # 4079
print(citydata[0])  # (1, 'Kabul', 'AFG', 'Kabol', 1780000)

# (4) 파이썬 데이터 : 2차원 튜플 => 데이터 프레임
# 데이터프레임명 = pd.DataFrame(데이터, columns=[컬럼명1, 컬럼명2,...])
df = pd.DataFrame(citydata,columns=['Id', 'Name', 'CountryCode', 'District', 'Population'])

print(df.head())

# (5) csv 저장
df.to_csv('output/city10A.csv', index = False)
df[['Name', 'Population']].to_csv('output/city10B.csv', index = False)

# 데이터베이스 닫기
conn.close()