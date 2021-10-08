# 부동산 가격 크롤링
import os
import sys
import numpy as np
import pandas as pd
import requests # 크롤링에 사용하는 패키지
import urllib.request
from bs4 import BeautifulSoup # html 변환에 사용함
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import seaborn as sns

## 법정동 코드
### 법정동코드 불러오기
codes = pd.read_csv('data/부동산/법정동코드.txt', sep = "\t", engine='python', encoding = "cp949")

### 원하는 지역 검색
def search_dong():
    keyword = input('동을 입력하세요 : ')
    return codes['법정동명'][codes['법정동명'].str.contains(keyword)]

## 핫플레이스 구역 별 법정동 지정
###핫플레이스 구역별
hots = pd.read_csv('data/hot_place_list.csv')

hots.columns

dong_dict = {'홍대': '서울특별시 마포구 합정동',
             '연남': '서울특별시 마포구 연남동',
             '이태원': '서울특별시 용산구 이태원동',
             '종로': '서울특별시 종로구 익선동',
             '을지로': '서울특별시 중구 인현동2가',
             '성수': '서울특별시 성동구 성수동1가',
             '한남': '서울특별시 용산구 한남동',
             '청담': '서울특별시 강남구 청담동',
             '신사': '서울특별시 강남구 신사동',
             '삼청': '서울특별시 종로구 견지동',
             '서촌': '서울특별시 종로구 청운동',
             '장충': '서울특별시 중구 신당동',
             '반포': '서울특별시 서초구 방배동',
             '혜화': '서울특별시 종로구 명륜2가',
             '신촌': '서울특별시 마포구 노고산동',
             '강남': '서울특별시 강남구 역삼동'}

search_dong()

def sise(dong, period=2):
    '''
    시세 데이터를 크롤링 하는 함수.
    dong : 검색하고 싶은 지역의 법정동 명
    period : 기간 설정 (1: 최근 3년간, 2: 최근 5년간, 3: 전체)
    '''
    code = int(codes['법정동코드'][codes['법정동명'] == dong])
    period = 2  # 최근 3년간 : 1, 최근 5년간 : 2, 전체 : 3
    url = f'https://api.kbland.kr/land-price/price/regionPrice/detailChartList?%EC%A1%B0%ED%9A%8C%EA%B8%B0%EA%B0%84%EA%B5%AC%EB%B6%84={period}&%EB%B2%95%EC%A0%95%EB%8F%99%EC%BD%94%EB%93%9C={code}&%EB%A0%88%EB%B2%A8=15&%EC%8B%9C%EC%84%B8%EC%83%81%ED%83%9C%EA%B5%AC%EB%B6%84=2&webCheck=Y'
    print(f'{place} : {dong} 크롤링 중입니다.')
    response = requests.get(url)
    data = json.loads(response.text)

    return data

dong = '서울특별시 종로구 견지동'

sise(dong)

## 지역별 부동산 가격 크롤링

#dong = '서울특별시 마포구 연남동'
df_total = pd.DataFrame()
for place in dong_dict.keys():
    dong = dong_dict[place]
    data = sise(dong)
    time.sleep(3)
    if 'message' in data['dataBody']:
        df_total[place] = 0
    else:
        df = pd.DataFrame()
        for i in range(len(data['dataBody']['data']['시세'])):
            df_temp = pd.DataFrame(data['dataBody']['data']['시세'][i]['items'])
            df = pd.concat([df, df_temp])
#         df = df.set_index('기준년월')
#         df_total = pd.concat([df_total, df['매매평균가']], axis=1)
        if df['매매평균가'].isnull().sum() > 0:
            #df.fillna(0)
            df_total[place] = 0
        else:
            df_total[place] = df['매매평균가']
df_total = df_total.set_index(df['기준년월'])

## 지역별 부동산 가격 시각화
for place in hots:
    sns.lineplot(x=df_total.index,  y=place, data = df_total)

## 파일 csv 저장하기
df_total.to_csv('data/부동산/매매평균가.csv', encoding='utf-8-sig')




