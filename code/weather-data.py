# 서울시 날씨 데이터

## 서울시 날씨 월별/ 분기별  데이터 전처리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm

## 한글 셋팅
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    f_path = '/Library/Fonts/Arial Unicode.ttf'
elif platform.system() == 'Windows':
    f_path = 'c:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)

print('Hangul font is set!')

## 파일 읽기 
df = pd.read_excel('./Report_month.xls')

df.columns

## 데이터 새로 생성하기
df_month = df[['기간', '구분', '기온(℃)', '강수량(mm)', '평균운량(10%)']]
df_month

df_month.info()

df_month = df_month.drop(0)

## 데이터 전처리: type 변환
df_month['강수량(mm)'] = df_month['강수량(mm)'].replace('-', 0)

df_month['기온(℃)'] = df_month['기온(℃)'].astype(float)

## 데이터 엑셀로 저장하기
df_month.to_csv('weather_month.csv')

## 월별로 데이터 합치기
df_month['월'] = pd.to_datetime(df_month['기간'])
df_month['월'] = df_month['월'].dt.month
df_month = df_month.groupby('월').mean()
df_month

## 분기별로 데이터 합치기
def season(month):
    ss = ['겨울', '봄', '여름', '가을']
    if month == 12:
        return ss[0]
    return ss[month//3]

## 분기별로 합치기
df_season = df_month
df_season['season'] = df_season.index
df_season['season'] = df_season['season'].apply(season)
df_season = df_season.groupby('season').mean()
df_season = df_season.reindex(['봄', '여름', '가을', '겨울'])

## 숫자 깔끔하게 정리하기
df_season = df_season.round(0)


# 서울시 날씨 월별/ 분기별 데이터 시각화

## bar plot
test = ['기온(℃)', '강수량(mm)', '평균운량(10%)']

for i in test:
    plt.figure(figsize=(12,8))
    plt.bar(df_month[i].index, df_month[i].values)
    plt.xlabel(i)
plt.savefig('weather_month_1.png')
plt.show()

## scatter plot
plt.figure(figsize=(12, 8))
sns.pairplot(df_month)
plt.savefig('weather_month_2.png')
plt.show()

## line plot
test = ['기온(℃)', '강수량(mm)', '평균운량(10%)']
for i in test:
    sns.lineplot(x=df_month.index,  y=i, data = df_month, label=i)
    plt.legend()
plt.savefig('weather_month_3.png')
plt.show()

## joint plot
test = ['기온(℃)', '강수량(mm)', '평균운량(10%)']

plt.figure(figsize=(12, 8))
sns.jointplot(df_month['기온(℃)'], df_month['강수량(mm)'], kind='kde')
plt.show()

--------------------------------------------------------------------------

## 서울시 날씨 년별 데이터 전처리

## 파일  읽기
df2 = pd.read_csv('./weather_year.csv')

## 필요한 데이터만 빼오기
df_year = df2[['기간', '기온(℃)', '강수량(mm)', '평균운량(10%)']]

df_year = df_year.drop(0)

## 데이터 타입 바꾸기
df_year['평균운량(10%)'] = df_year['평균운량(10%)'].astype(float)

## 열을 행으로 바꾸고, 데이터 숫자 깔끔하게 처리하기
df_year = df_year.set_index('기간')

df_year = df_year.round(0)

## 파일 새로 저장하기
df_year.to_csv('weather_year.csv')

# 서울시 날씨 년별 데이터 시각화

## bar plot
test = ['기온(℃)', '강수량(mm)', '평균운량(10%)']

for i in test:
    plt.figure(figsize=(12,8))
    plt.bar(df_year[i].index, df_year[i].values)
    plt.xlabel(i)
plt.savefig('weather_year_1.png')
plt.show()

## pair plot
sns.pairplot(df_year)
plt.savefig('weather_year_2.png')
plt.show()

## line plot
test = ['기온(℃)', '강수량(mm)', '평균운량(10%)']
for i in test:
    sns.lineplot(x=df_month.index,  y=i, data = df_month, label=i)
    plt.legend()
plt.savefig('weather_year_3.png')
plt.show()

## 네이버 데이터 api와 서울시 년별 데이터 합치기
plt.figure(figsize=(12,8))
sns.lineplot(x = test.index, y =test.sum(axis=1), sort=False, label='검색량')
sns.lineplot(x=df_season.index,  y=df_season.sum(axis=1), data = df_season, label='날씨')
plt.xlabel('계절')
plt.legend()
plt.savefig('season_data_1.png')

## 지하철 유동인구와 서울시 년별 데이터 합치기
plt.figure(figsize=(12,8))
sns.lineplot(x = pair_df.index, y = pair_df.sum(axis=1), data = pair_df, label='유동인구')
sns.lineplot(x=test_year.index,  y=test_year['기온(℃)'], data = test_year, label='기온(℃)')
plt.legend()
plt.savefig('season_data_2.png')
plt.show()
