# 인스타그램 크롤링 데이터 전처리

## 인스타그램 맛집 해시태그 데이터 전처리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 파일 불러오기
ins_data = pd.read_excel('./ins_tag_place.xlsx')
ins_data

# DataFrame으로 만들어주기
df = pd.DataFrame(ins_data)

# index 설정하기
df = df.set_index('게시일')
df

# 데이터 count, unique 등과 정보 확인하기
df.describe()
df.info()

# 지역별 구분에 맞춰 해시태그 데이터 분할하기

## 홍대
list_1 = ['홍대', '홍대맛집', '합정맛집', '망원맛집', '홍대술집', '합정역맛집']
test_1 = '|'.join(list_1)
df_1 = df[df['해시태그'].str.contains(test_1)]
df_1.index = range(len(df_1))
print('홍대 해시태그 수 : ', len(df_1))
df_1

## 연남
list_2 = ['연남', '연남동맛집', '연남동카페', '연남동술집', '연희동맛집', '연희동카페']
test_2 = '|'.join(list_2)
df_2 = df[df['해시태그'].str.contains(test_2)]
df_2.index = range(len(df_2))
print('연남 해시태그 수 : ', len(df_2))
df_2

## 이태원
list_3 = ['이태원', '이태원맛집', '경리단길', '이태원술집', '해방촌맛집', '후암동맛집']
test_3 = '|'.join(list_3)
df_3 = df[df['해시태그'].str.contains(test_3)]
df_3.index = range(len(df_3))
print('이태원 해시태그 수 : ', len(df_3))
df_3

## 종로
list_4 = ['종로', '인사동맛집', '익선동맛집', '종로맛집', '종로3가맛집', '익선동카페']
test_4 = '|'.join(list_4)
df_4 = df[df['해시태그'].str.contains(test_4)]
df_4.index = range(len(df_4))
print('종로 해시태그 수 : ', len(df_4))
df_4

## 을지로
list_5 = ['을지로', '을지로맛집', '을지로3가맛집', '을지로입구맛집', '충무로맛집', '을지로카페']
test_5 = '|'.join(list_5)
df_5 = df[df['해시태그'].str.contains(test_5)]
df_5.index = range(len(df_5))
print('을지로 해시태그 수 : ', len(df_5))
df_5

## 성수
list_6 = ['성수', '성수맛집', '성수동맛집', '서울숲맛집', '성수역맛집', '성수카페']
test_6 = '|'.join(list_6)
df_6 = df[df['해시태그'].str.contains(test_6)]
df_6.index = range(len(df_6))
print('성수 해시태그 수 : ', len(df_6))
df_6

## 한남
list_7 = ['한남', '한남동맛집', '한남동카페', '한남맛집', '옥수동맛집', '금호동맛집']
test_7 = '|'.join(list_7)
df_7 = df[df['해시태그'].str.contains(test_7)]
df_7.index = range(len(df_7))
print('한남 해시태그 수 : ', len(df_7))
df_7

## 청담
list_8 = ['청담', '청담동맛집', '청담맛집', '청담카페', '도산공원맛집', '학동역맛집']
test_8 = '|'.join(list_8)
df_8 = df[df['해시태그'].str.contains(test_8)]
df_8.index = range(len(df_8))
print('청담 해시태그 수 : ', len(df_8))
df_8

## 신사
list_9 = ['신사', '신사역맛집', '가로수길맛집', '신사맛집', '가로수길카페', '압구정맛집']
test_9 = '|'.join(list_9)
df_9 = df[df['해시태그'].str.contains(test_9)]
df_9.index = range(len(df_9))
print('신사 해시태그 수 : ', len(df_9))
df_9

## 삼청
list_10 = ['삼청', '삼청동맛집', '경복궁맛집', '안국역맛집', '북촌맛집', '북촌카페']
test_10 = '|'.join(list_10)
df_10 = df[df['해시태그'].str.contains(test_10)]
df_10.index = range(len(df_10))
print('삼청 해시태그 수 : ', len(df_10))
df_10

## 서촌
list_11 = ['서촌', '서촌맛집', '서촌카페', '부암동맛집', '부암동카페', '경복궁역맛집']
test_11 = '|'.join(list_11)
df_11 = df[df['해시태그'].str.contains(test_11)]
df_11.index = range(len(df_11))
print('서촌 해시태그 수 : ', len(df_11))
df_11

## 장충
list_12 = ['장충', '장충동맛집', '약수역맛집', '신당동맛집', '신당역맛집', '청구역맛집']
test_12 = '|'.join(list_12)
df_12 = df[df['해시태그'].str.contains(test_12)]
df_12.index = range(len(df_12))
print('장충 해시태그 수 : ', len(df_12))
df_12

## 반포
list_13 = ['반포', '서래마을맛집', '이수역맛집', '방배동맛집', '이수맛집', '반포맛집']
test_13 = '|'.join(list_13)
df_13 = df[df['해시태그'].str.contains(test_13)]
df_13.index = range(len(df_13))
print('반포 해시태그 수 : ', len(df_13))
df_13

## 혜화
list_14 = ['혜화', '혜화맛집', '대학로맛집', '혜화역맛집', '대학로카페', '혜화카페']
test_14 = '|'.join(list_14)
df_14 = df[df['해시태그'].str.contains(test_14)]
df_14.index = range(len(df_14))
print('혜화 해시태그 수 : ', len(df_14))
df_14

## 신촌
list_15 = ['신촌', '신촌맛집', '신촌역맛집', '이대맛집', '신촌술집', '신촌카페']
test_15 = '|'.join(list_15)
df_15 = df[df['해시태그'].str.contains(test_15)]
df_15.index = range(len(df_15))
print('신촌 해시태그 수 : ', len(df_15))
df_15

## 강남
list_16 = ['강남', '강남맛집', '강남역맛집', '강남역술집', '강남술집', '강남카페']
test_16 = '|'.join(list_16)
df_16 = df[df['해시태그'].str.contains(test_16)]
df_16.index = range(len(df_16))
print('강남 해시태그 수 : ', len(df_16))
df_16

# 데이터 시각화 및 한글 셋팅
import seaborn as sns
import matplotlib.pyplot as plt
import platform

from matplotlib import font_manager, rc
%matplotlib inline

## 운영체제별 글꼴 세팅

path = "c:/Windows/Fonts/malgun.ttf"
if platform.system() == 'Darwin':
    font_name = 'Apple SD Gothic Neo'
    rc('font', family='Apple SD Gothic Neo')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    font_name = font_manager.FontProperties(fname="/usr/share/fonts/nanumfont/NanumGothic.ttf")
    rc('font', family="NanumGothic")

# 데이터 가공하기
df1_rate = (len(df_1)/100)
df2_rate = (len(df_2)/100)
df3_rate = (len(df_3)/100)
df4_rate = (len(df_4)/100)
df5_rate = (len(df_5)/100)
df6_rate = (len(df_6)/100)
df7_rate = (len(df_7)/100)
df8_rate = (len(df_8)/100)
df9_rate = (len(df_9)/100)
df10_rate = (len(df_10)/100)
df11_rate = (len(df_11)/100)
df12_rate = (len(df_12)/100)
df13_rate = (len(df_13)/100)
df14_rate = (len(df_14)/100)
df15_rate = (len(df_15)/100)
df16_rate = (len(df_16)/100)

# 인스타그램 맛집 해시태그 Barplot
x = ['홍대', '연남', '이태원', '종로', '을지로', '성수', '한남', '청담', '신사', '삼청', '서촌', '장충', '반포', '혜화', '신촌', '강남']
y = [df1_rate, df2_rate, df3_rate, df4_rate, df5_rate, df6_rate, df7_rate, df8_rate, df9_rate, df10_rate, df11_rate, df12_rate, df13_rate, df14_rate, df15_rate, df16_rate]

plt.figure(figsize=(12,12))
plt.title('서울 핫플레이스 인스타그램 맛집 언급 비율', fontdict={'fontsize' : 20})
sns.barplot(x=x, y=y)
plt.savefig('ins_hotplace_restaurant.png')
plt.show()

# 인스타그램 카페 해시태그도 지역별 구분에 맞춰 똑같이 진행

# 인스타그램 맛집, 카페 해시태그 Barplot 함께 보여주기
x = ['홍대', '연남', '이태원', '종로', '을지로', '성수', '한남', '청담', '신사', '삼청', '서촌', '장충', '반포', '혜화', '신촌', '강남']
y1 = [df1_rate, df2_rate, df3_rate, df4_rate, df5_rate, df6_rate, df7_rate, df8_rate, df9_rate, df10_rate, df11_rate, df12_rate, df13_rate, df14_rate, df15_rate, df16_rate]
y2 = [df2_1_rate, df2_2_rate, df2_3_rate, df2_4_rate, df2_5_rate, df2_6_rate, df2_7_rate, df2_8_rate, df2_9_rate, df2_10_rate, df2_11_rate, df2_12_rate, df2_13_rate, df2_14_rate, df2_15_rate, df2_16_rate]

plt.figure(figsize=(12, 8))

plt.subplot(211) # 도화지 나누기 2행 1열 그래프의 첫번째
sns.barplot(x=x, y=y1)
plt.title('서울 핫플레이스 인스타그램 맛집 언급 비율')
plt.savefig('ins_hotplace_restaurant.png')

plt.subplot(212) # 도화지 나누기 2행 1열 그래프의 두번째
sns.barplot(x=x, y=y2)
plt.title('서울 핫플레이스 인스타그램 카페 언급 비율')
plt.savefig('ins_hotplace_cafe.png')

plt.tight_layout() # 여백줄이기
plt.show()

# 인스타그램 해시태그 Scatter plot
plt.figure(figsize=(12,8))
sns.scatterplot(pair_df['맛집'], pair_df['카페'],hue=pair_df['맛집'])
plt.savefig('ins_hotplace_total.png')
plt.show()

# 인스타그램 해시태그 Pair plot
## 변수명 설정
place_nm = ['홍대', '연남', '이태원', '종로', '을지로', '성수', '한남', '청담', '신사', '삼청', '서촌', '장충', '반포', '혜화', '신촌', '강남']
place_nm

restaurant_tags = [df1_rate, df2_rate, df3_rate, df4_rate, df5_rate, df6_rate, df7_rate, df8_rate, df9_rate, df10_rate, df11_rate, df12_rate, df13_rate, df14_rate, df15_rate, df16_rate]
restaurant_tags

cafe_tags =[df2_1_rate, df2_2_rate, df2_3_rate, df2_4_rate, df2_5_rate, df2_6_rate, df2_7_rate, df2_8_rate, df2_9_rate, df2_10_rate, df2_11_rate, df2_12_rate, df2_13_rate, df2_14_rate, df2_15_rate, df2_16_rate]
cafe_tags

# 변수명 DataFrame으로 만들어주기
pair_df = pd.DataFrame({'맛집' : restaurant_tags, '카페' : cafe_tags}, index = place_nm)
pair_df

# 각 컬럼간 모든 scatter plot을 그리는 pairplot
plt.figure(figsize=(12, 8))
sns.pairplot(pair_df)
plt.savefig('ins_hotplace.png')
plt.show()
