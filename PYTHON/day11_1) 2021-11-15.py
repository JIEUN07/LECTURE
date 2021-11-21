# print("Helloworld")
'''
판다스
파이썬계 엑셀
https://pandas.pydata.org/
시리즈(column) + 데이터 프레임(table)
'''

'''
넘파이
Numeric Python
통계, 확률, 선형대수학을 지원하는 메서드포함
https://numpy.org/
'''
# 설치파일 확인 pip list

import pandas as pd
import numpy as np

# csv 파일 불러오기 
# 파이썬의 구조(데이터 프레임)으로 바꿈
# 파이썬의 데이터 구조 => 리스트, 튜플, 집합, 딕셔너리
# 데이터 프레임명 = pd.read_csv(url)
df = pd.read_csv('data/data.csv')
print(df)

print(df.columns)
# Index(['class', 'name', 'kor', 'eng', 'mat', 'bio'], dtype='object')
print(df.index)
# RangeIndex(start=0, stop=12, step=1)
# 전체구조 확인
print(df.shape)
# (12, 6)

import os
print(os.getcwd()) # 현재 작업폴더 확인

# 리스트[start:end:step]
# mylist[:3]
mylist = [10, 20, 30, 40, 50]
print(mylist[0:2]) # [10, 20]

# 데이터프레임 컬럼 인덱스
# 데이처프레임명[컬럼명]
print(df['name'])  # 시리즈로 반환

# print('='*50) 이건 '=' 50개 출력 (프린트 여러개할때 가독성 좋게 함)
print(df[['name', 'class']])  # 두개이상일때 데이터프레임으로 반환

# 데이터프레임 행 인덱스
# 데이터프레임.head(n) - 앞에서 n개 행
# 데이터프레임.tail(n) - 뒤에서 n개 행
# 데이터프레임.loc[start:end] - location 행이름
# 데이터프레임.iloc[start:end] - index location 숫자인덱스

print(df.head(2)) # 디폴트 5개
print(df.tail(2))
print(df.loc[4:6])  # 3개 4,5,6 행 다나옴
print(df.iloc[4:6])  # 2개 마지막 6번 버림

# 특정행의 특정열 인덱스
# 데이터프레임.loc[start:end, start:end] - location 행이름
# 데이터프레임.iloc[start:end, start:end] - index location 숫자인덱스
print(df.iloc[4:6])

# 1반의 이름과 국어점수만 표시
print(df.loc[0:5, 'class':'kor'])
print(df.iloc[0:6, 0:3])

# 특정행의 특정열
# 데이터프레임.loc[[행이름1, 행이름2...], [열이름1, 열이름2...]]
# 데이터프레임.iloc[[인덱스1, 인덱스2...], [인덱스1, 인덱스2..]]

# 1반 kor, math 컬럼
print(df.loc[0:5, ['class','kor','mat']])
print(df.iloc[0:6, [0, 2, 4]])

# csv파일로 저장
# 데이터프레임.ot_csv(url)
# 1반의 이름, 국어, 영어, 수학 => output/data2.csv
print(df.loc[0:5, 'name':'mat'])


# 현재폴더기준 output 폴더 생성
try:
    os.mkdir('output')
except:
    print('폺더가 이미 생성되었습니다.')
df2 = df.loc[0:5, 'name':'mat']
df2.to_csv('output/data2.csv', index= False) # index = False 행이름 저장안함

# 퀴즈
# population.csv에서 마지막 10개만 잘라서
# output/population.csv로 저장
df_pop = pd.read_csv('data/population.csv')
print(df_pop.shape) # (51, 2)
df_pop1 = df_pop.tail(10)
# df_pop2 = df_pop.loc[41:]
# df_pop2 = df_pop.iloc[41:]
print(df_pop1)
df_pop1.to_csv('output/population2.csv', index=False)


