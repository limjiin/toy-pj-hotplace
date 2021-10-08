# folium을 활용한  지도 시각화

# 지도 좌표 설정
## 구글링을 활용하여 얻은 파일을 서울 지역에 맞춰  재가공함
{"type":"FeatureCollection",
  "features":[
{"type":"Feature","properties":{"code":"11240","name":"송파구","name_eng":"Songpa-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.0690698130372,37.522279423505026],[127.10087519791962,37.524841220167055],[127.1116764203608,37.540669955324965],[127.12123165719615,37.52528270089],[127.14672806823502,37.51415680680291],[127.1634944215765,37.497445406097484],[127.14206058413274,37.47089819098501],[127.12440571080893,37.46240445587048],[127.11117085201238,37.485708381512445],[127.0719146000724,37.50224013587669],[127.0690698130372,37.522279423505026]]]}},
{"type":"Feature","properties":{"code":"11230","name":"강남구","name_eng":"Gangnam-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.05867359288398,37.52629974922568],[127.0690698130372,37.522279423505026],[127.0719146000724,37.50224013587669],[127.11117085201238,37.485708381512445],[127.12440571080893,37.46240445587048],[127.09842759318751,37.45862253857461],[127.08640440578156,37.472697935184655],[127.0559170481904,37.4659228914077],[127.03621915098798,37.48175802427603],[127.01397119667513,37.52503988289669],[127.02302831890559,37.53231899582663],[127.05867359288398,37.52629974922568]]]}},
{"type":"Feature","properties":{"code":"11220","name":"서초구","name_eng":"Seocho-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.01397119667513,37.52503988289669],[127.03621915098798,37.48175802427603],[127.0559170481904,37.4659228914077],[127.08640440578156,37.472697935184655],[127.09842759318751,37.45862253857461],[127.09046928565951,37.44296826114185],[127.06778107605433,37.426197424057314],[127.04957232987142,37.42805836845694],[127.03881782597922,37.45382039851715],[126.99072073195462,37.455326143310025],[126.98367668291802,37.473856492692086],[126.98223807916081,37.509314966770326],[127.01397119667513,37.52503988289669]]]}},
{"type":"Feature","properties":{"code":"11210","name":"관악구","name_eng":"Gwanak-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.98367668291802,37.473856492692086],[126.99072073195462,37.455326143310025],[126.96520439085143,37.438249784006246],[126.95000001010182,37.43613451165719],[126.93084408056525,37.447382928333994],[126.9167728146601,37.45490566423789],[126.90156094129895,37.47753842789901],[126.90531975801812,37.48218087575429],[126.94922661389508,37.49125437495649],[126.9725891850662,37.472561363278125],[126.98367668291802,37.473856492692086]]]}},
{"type":"Feature","properties":{"code":"11200","name":"동작구","name_eng":"Dongjak-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.98223807916081,37.509314966770326],[126.98367668291802,37.473856492692086],[126.9725891850662,37.472561363278125],[126.94922661389508,37.49125437495649],[126.90531975801812,37.48218087575429],[126.92177893174825,37.494889877415176],[126.92810628828279,37.51329595732015],[126.95249990298159,37.51722500741813],[126.98223807916081,37.509314966770326]]]}},
{"type":"Feature","properties":{"code":"11190","name":"영등포구","name_eng":"Yeongdeungpo-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.89184663862764,37.547373974997114],[126.94566733083212,37.526617542453366],[126.95249990298159,37.51722500741813],[126.92810628828279,37.51329595732015],[126.92177893174825,37.494889877415176],[126.90531975801812,37.48218087575429],[126.89594776782485,37.504675281309176],[126.88156402353862,37.513970034765684],[126.88825757860099,37.54079733630232],[126.89184663862764,37.547373974997114]]]}},
{"type":"Feature","properties":{"code":"11180","name":"금천구","name_eng":"Geumcheon-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.90156094129895,37.47753842789901],[126.9167728146601,37.45490566423789],[126.93084408056525,37.447382928333994],[126.9025831711697,37.434549366349124],[126.87683271502428,37.482576591607305],[126.90156094129895,37.47753842789901]]]}},
{"type":"Feature","properties":{"code":"11170","name":"구로구","name_eng":"Guro-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.82688081517314,37.50548972232896],[126.88156402353862,37.513970034765684],[126.89594776782485,37.504675281309176],[126.90531975801812,37.48218087575429],[126.90156094129895,37.47753842789901],[126.87683271502428,37.482576591607305],[126.84762676054953,37.47146723936323],[126.83549485076196,37.474098236975095],[126.82264796791348,37.4878476492147],[126.82504736331406,37.50302612640443],[126.82688081517314,37.50548972232896]]]}},
{"type":"Feature","properties":{"code":"11160","name":"강서구","name_eng":"Gangseo-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.79575768552907,37.57881087633202],[126.80702115023597,37.60123001013228],[126.82251438477105,37.5880430810082],[126.85984199399667,37.571847855292745],[126.89184663862764,37.547373974997114],[126.88825757860099,37.54079733630232],[126.86637464321238,37.54859191094823],[126.86610073476395,37.52699964144669],[126.84257291943153,37.52373707805596],[126.8242331426722,37.53788078753248],[126.77324417717703,37.5459123450554],[126.76979180579352,37.55139183008809],[126.79575768552907,37.57881087633202]]]}},
{"type":"Feature","properties":{"code":"11150","name":"양천구","name_eng":"Yangcheon-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.8242331426722,37.53788078753248],[126.84257291943153,37.52373707805596],[126.86610073476395,37.52699964144669],[126.86637464321238,37.54859191094823],[126.88825757860099,37.54079733630232],[126.88156402353862,37.513970034765684],[126.82688081517314,37.50548972232896],[126.8242331426722,37.53788078753248]]]}},
{"type":"Feature","properties":{"code":"11140","name":"마포구","name_eng":"Mapo-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.90522065831053,37.57409700522574],[126.93898161798973,37.552310003728124],[126.96358226710812,37.55605635475154],[126.96448570553055,37.548705692021635],[126.94566733083212,37.526617542453366],[126.89184663862764,37.547373974997114],[126.85984199399667,37.571847855292745],[126.88433284773288,37.588143322880526],[126.90522065831053,37.57409700522574]]]}},
{"type":"Feature","properties":{"code":"11130","name":"서대문구","name_eng":"Seodaemun-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.9524752030572,37.60508692737045],[126.95565425846463,37.576080790881456],[126.96873633279075,37.56313604690827],[126.96358226710812,37.55605635475154],[126.93898161798973,37.552310003728124],[126.90522065831053,37.57409700522574],[126.9524752030572,37.60508692737045]]]}},
{"type":"Feature","properties":{"code":"11120","name":"은평구","name_eng":"Eunpyeong-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.9738864128702,37.62949634786888],[126.95427017006129,37.622033431339425],[126.9524752030572,37.60508692737045],[126.90522065831053,37.57409700522574],[126.88433284773288,37.588143322880526],[126.90396681003595,37.59227403419942],[126.90303066177668,37.609977911401344],[126.91455481429648,37.64150050996935],[126.956473797387,37.652480737339445],[126.9738864128702,37.62949634786888]]]}},
{"type":"Feature","properties":{"code":"11110","name":"노원구","name_eng":"Nowon-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.0838752703195,37.69359534202034],[127.09706391309695,37.686383719372294],[127.09440766298717,37.64713490473045],[127.11326795855199,37.639622905315925],[127.10782277688129,37.61804244241069],[127.07351243825278,37.61283660342313],[127.05209373568619,37.62164065487782],[127.04358800895609,37.62848931298715],[127.05800075220091,37.64318263878276],[127.05288479710485,37.68423857084347],[127.0838752703195,37.69359534202034]]]}},
{"type":"Feature","properties":{"code":"11100","name":"도봉구","name_eng":"Dobong-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.05288479710485,37.68423857084347],[127.05800075220091,37.64318263878276],[127.04358800895609,37.62848931298715],[127.01465935892466,37.64943687496812],[127.02062116141389,37.667173575971205],[127.01039666042071,37.681894589603594],[127.01795099203432,37.69824412775662],[127.05288479710485,37.68423857084347]]]}},
{"type":"Feature","properties":{"code":"11090","name":"강북구","name_eng":"Gangbuk-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.99383903424,37.676681761199085],[127.01039666042071,37.681894589603594],[127.02062116141389,37.667173575971205],[127.01465935892466,37.64943687496812],[127.04358800895609,37.62848931298715],[127.05209373568619,37.62164065487782],[127.03892400992301,37.609715611023816],[127.0128154749523,37.613652243470256],[126.98672705513869,37.63377641288196],[126.9817452676551,37.65209769387776],[126.99383903424,37.676681761199085]]]}},
{"type":"Feature","properties":{"code":"11080","name":"성북구","name_eng":"Seongbuk-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.977175406416,37.62859715400388],[126.98672705513869,37.63377641288196],[127.0128154749523,37.613652243470256],[127.03892400992301,37.609715611023816],[127.05209373568619,37.62164065487782],[127.07351243825278,37.61283660342313],[127.07382707099227,37.60401928986419],[127.042705222094,37.59239437593391],[127.02527254528003,37.57524616245249],[126.99348293358314,37.588565457216156],[126.98879865992384,37.6118927319756],[126.977175406416,37.62859715400388]]]}},
{"type":"Feature","properties":{"code":"11070","name":"중랑구","name_eng":"Jungnang-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.07351243825278,37.61283660342313],[127.10782277688129,37.61804244241069],[127.1201246020114,37.60178457598188],[127.10304174249214,37.57076342290955],[127.08068541280403,37.56906425519017],[127.07382707099227,37.60401928986419],[127.07351243825278,37.61283660342313]]]}},
{"type":"Feature","properties":{"code":"11060","name":"동대문구","name_eng":"Dongdaemun-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.02527254528003,37.57524616245249],[127.042705222094,37.59239437593391],[127.07382707099227,37.60401928986419],[127.08068541280403,37.56906425519017],[127.07421053024362,37.55724769712085],[127.05005601081567,37.567577612590846],[127.02547266349976,37.568943552237734],[127.02527254528003,37.57524616245249]]]}},
{"type":"Feature","properties":{"code":"11050","name":"광진구","name_eng":"Gwangjin-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.08068541280403,37.56906425519017],[127.10304174249214,37.57076342290955],[127.11519584981606,37.557533180704915],[127.1116764203608,37.540669955324965],[127.10087519791962,37.524841220167055],[127.0690698130372,37.522279423505026],[127.05867359288398,37.52629974922568],[127.07421053024362,37.55724769712085],[127.08068541280403,37.56906425519017]]]}},
{"type":"Feature","properties":{"code":"11040","name":"성동구","name_eng":"Seongdong-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.02547266349976,37.568943552237734],[127.05005601081567,37.567577612590846],[127.07421053024362,37.55724769712085],[127.05867359288398,37.52629974922568],[127.02302831890559,37.53231899582663],[127.01070894177482,37.54118048964762],[127.02547266349976,37.568943552237734]]]}},
{"type":"Feature","properties":{"code":"11030","name":"용산구","name_eng":"Yongsan-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.01070894177482,37.54118048964762],[127.02302831890559,37.53231899582663],[127.01397119667513,37.52503988289669],[126.98223807916081,37.509314966770326],[126.95249990298159,37.51722500741813],[126.94566733083212,37.526617542453366],[126.96448570553055,37.548705692021635],[126.98752996903328,37.55094818807139],[127.01070894177482,37.54118048964762]]]}},
{"type":"Feature","properties":{"code":"11020","name":"중구","name_eng":"Jung-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[127.02547266349976,37.568943552237734],[127.01070894177482,37.54118048964762],[126.98752996903328,37.55094818807139],[126.96448570553055,37.548705692021635],[126.96358226710812,37.55605635475154],[126.96873633279075,37.56313604690827],[127.02547266349976,37.568943552237734]]]}},
{"type":"Feature","properties":{"code":"11010","name":"종로구","name_eng":"Jongno-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":[[[126.9738864128702,37.62949634786888],[126.977175406416,37.62859715400388],[126.98879865992384,37.6118927319756],[126.99348293358314,37.588565457216156],[127.02527254528003,37.57524616245249],[127.02547266349976,37.568943552237734],[126.96873633279075,37.56313604690827],[126.95565425846463,37.576080790881456],[126.9524752030572,37.60508692737045],[126.95427017006129,37.622033431339425],[126.9738864128702,37.62949634786888]]]}}]}

# 인스타그램 해시태그 데이터 전처리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data 열기
ins_data = pd.read_excel('./ins_tag_place.xlsx')
ins_data

# DataFrame 만들기
df = pd.DataFrame(ins_data)
df = df.set_index('게시일')
df

## 지역 구분
- 1 : 송파구
- 2 : 강남구
- 3 : 서초구
- 4 : 관악구
- 5 : 동작구
- 6 : 영등포구
- 7 : 금천구
- 8 : 구로구
- 9 : 강서구
- 10 : 양천구
- 11 : 마포구
- 12 : 서대문구
- 13 : 은평구
- 14 : 노원구
- 15 : 도봉구
- 16 : 강북구
- 17 : 성북구
- 18 : 중랑구
- 19 : 동대문구
- 20 : 광진구
- 21 : 성동구
- 22 : 용산구
- 23 : 중구
- 24 : 종로구

# 서울 자치구에 맞춰 지역별 데이터 재배열

## 송파구
df_1 = []
print('송파구 해시태그 수 : ', len(df_1))
df_1

## 강남구
list_2 = ['신사', '신사역맛집', '가로수길맛집', '신사맛집', '가로수길카페', '압구정맛집', '청담', '청담동맛집', '청담맛집', '청담카페', '도산공원맛집', '학동역맛집']
test_2 = '|'.join(list_2)
df_2 = df[df['해시태그'].str.contains(test_2)]
df_2.index = range(len(df_2))
print('강남구 해시태그 수 : ', len(df_2))
df_2

## 서초구
list_3 = ['반포', '서래마을맛집', '이수역맛집', '방배동맛집', '이수맛집', '반포맛집', '강남', '강남맛집', '강남역맛집', '강남역술집', '강남술집', '강남카페']
test_3 = '|'.join(list_3)
df_3 = df[df['해시태그'].str.contains(test_3)]
df_3.index = range(len(df_3))
print('서초구 해시태그 수 : ', len(df_3))
df_3

## 관악구
df_4 = []
print('관악구 해시태그 수 : ', len(df_4))
df_4

## 동작구
df_5 = []
print('동작구 해시태그 수 : ', len(df_5))
df_5

## 영등포구
df_6 = []
print('영등포구 해시태그 수 : ', len(df_6))
df_6

## 금천구
df_7 = []
print('금천구 해시태그 수 : ', len(df_7))
df_7

## 구로구
df_8 = []
print('구로구 해시태그 수 : ', len(df_8))
df_8

## 강서구
df_9 = []
print('강서구 해시태그 수 : ', len(df_9))
df_9

## 양천구
df_10 = []
print('양천구 해시태그 수 : ', len(df_10))
df_10

## 마포구
list_11 = ['홍대', '홍대맛집', '합정맛집', '망원맛집', '홍대술집', '합정역맛집', '연남', '연남동맛집', '연남동카페', '연남동술집', '연희동맛집', '연희동카페']
test_11 = '|'.join(list_11)
df_11 = df[df['해시태그'].str.contains(test_11)]
df_11.index = range(len(df_11))
print('마포구 해시태그 수 : ', len(df_11))
df_11

## 서대문구
list_12 = ['신촌', '신촌맛집', '신촌역맛집', '이대맛집', '신촌술집', '신촌카페']
test_12 = '|'.join(list_12)
df_12 = df[df['해시태그'].str.contains(test_12)]
df_12.index = range(len(df_12))
print('서대문구 해시태그 수 : ', len(df_12))
df_12

## 은평구
df_13 = []
print('은평구 해시태그 수 : ', len(df_13))
df_13

## 노원구
df_14 = []
print('노원구 해시태그 수 : ', len(df_14))
df_14

## 도봉구
df_15 = []
print('도봉구 해시태그 수 : ', len(df_15))
df_15

## 강북구
df_16 = []
print('강북구 해시태그 수 : ', len(df_16))
df_16

## 성북구
df_17 = []
print('성북구 해시태그 수 : ', len(df_17))
df_17

## 중랑구
df_18 = []
print('중랑구 해시태그 수 : ', len(df_18))
df_18

## 동대문구
df_19 = []
print('동대문구 해시태그 수 : ', len(df_19))
df_19

## 광진구
df_20 = []
print('광진구 해시태그 수 : ', len(df_20))
df_20

## 성동구
list_21 = ['성수', '성수맛집', '성수동맛집', '서울숲맛집', '성수역맛집', '성수카페']
test_21 = '|'.join(list_21)
df_21 = df[df['해시태그'].str.contains(test_21)]
df_21.index = range(len(df_21))
print('성동구 해시태그 수 : ', len(df_21))
df_21

## 용산구
list_22 = ['이태원', '이태원맛집', '경리단길', '이태원술집', '해방촌맛집', '후암동맛집', '한남', '한남동맛집', '한남동카페', '한남맛집', '옥수동맛집', '금호동맛집']
test_22 = '|'.join(list_22)
df_22 = df[df['해시태그'].str.contains(test_22)]
df_22.index = range(len(df_22))
print('용산구 해시태그 수 : ', len(df_22))
df_22

## 중구
list_23 = ['을지로', '을지로맛집', '을지로3가맛집', '을지로입구맛집', '충무로맛집', '을지로카페', '장충', '장충동맛집', '약수역맛집', '신당동맛집', '신당역맛집', '청구역맛집']
test_23 = '|'.join(list_23)
df_23 = df[df['해시태그'].str.contains(test_23)]
df_23.index = range(len(df_23))
print('중구 해시태그 수 : ', len(df_23))
df_23

## 종로구
list_24 = ['종로', '인사동맛집', '익선동맛집', '종로맛집', '종로3가맛집', '익선동카페', '삼청', '삼청동맛집', '경복궁맛집', '안국역맛집', '북촌맛집', '북촌카페', '서촌', '서촌맛집', '서촌카페', '부암동맛집', '부암동카페', '경복궁역맛집', '혜화', '혜화맛집', '대학로맛집', '혜화역맛집', '대학로카페', '혜화카페']
test_24 = '|'.join(list_24)
df_24 = df[df['해시태그'].str.contains(test_24)]
df_24.index = range(len(df_24))
print('종로구 해시태그 수 : ', len(df_24))
df_24

# 인스타그램 카페 해시태그도 똑같이 진행함

# 데이터 합치기
place_nm = ['송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구', '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구', '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구']
place_nm

restaurant_tags = [len(df_1), len(df_2), len(df_3), len(df_4), len(df_5), len(df_6), len(df_7), len(df_8), len(df_9), len(df_10), len(df_11), len(df_12), len(df_13), len(df_14), len(df_15), len(df_16), len(df_17), len(df_18), len(df_19), len(df_20), len(df_21), len(df_22), len(df_23), len(df_24)]
restaurant_tags

cafe_tags = [len(df2_1), len(df2_2), len(df2_3), len(df2_4), len(df2_5), len(df2_6), len(df2_7), len(df2_8), len(df2_9), len(df2_10), len(df2_11), len(df2_12), len(df2_13), len(df2_14), len(df2_15), len(df2_16), len(df2_17), len(df2_18), len(df2_19), len(df_20), len(df2_21), len(df2_22), len(df2_23), len(df2_24)]
cafe_tags

pair_df = pd.DataFrame({'자치구' : place_nm, '맛집' : restaurant_tags, '카페' : cafe_tags})
# pair_df = pair_df.rename_axis('자치구')
pair_df

# 네이버 데이터 API 전처리
import platform
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    f_path = '/Library/Fonts/Arial Unicode.ttf'
elif platform.system() == 'Windows':
    f_path = 'c:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=f_path).get_name()
rc('font', family=font_name)

print('Hangul font is set!')

# 엑셀 파일 가져오기
df3 = pd.read_csv('./total_search1.csv')
df3.set_index('period', inplace=True)

# 데이터 재가공하기
## 자치구별 데이터 추가

### 데이터가 없는 경우
df3['광진구'] = 0
df3

### 데이터가 있는 경우는 기존 데이터를 합쳐서 새로운 열 추가
df3['종로구'] = df3['삼청'] + df3['서촌'] + df3['혜화'] + df3['종로']
df3

### 기존 데이터 삭제하기
df3 = df3.drop(['삼청', '서촌', '혜화', '종로'], axis=1)
df3

## 행을 index로 설정하기
df3['period'] = df3.index
df3

# 연도별로 데이터 묶기
total_2016 = df3.sum()
total_2016 = pd.DataFrame(total_2016)
total_2016 = total_2016.drop('period')
total_2016

total_2017 = df3.sum()
total_2017 = pd.DataFrame(total_2017)
total_2017 = total_2017.drop('period')
total_2017

total_2018 = df3.sum()
total_2018 = pd.DataFrame(total_2018)
total_2018 = total_2018.drop('period')
total_2018

total_2019 = df3.sum()
total_2019 = pd.DataFrame(total_2019)
total_2019 = total_2019.drop('period')
total_2019

total_2020 = df3.sum()
total_2020 = pd.DataFrame(total_2020)
total_2020 = total_2020.drop('period')
total_2020

total_2021 = df3.sum()
total_2021 = pd.DataFrame(total_2021)
total_2021 = total_2021.drop('period')
total_2021

# 다른 데이터로 똑같이 처리하기

# 네이버 데이터 API 합치기
total_2016.columns=['data']
total_2016 = total_2016.reset_index()
total_2016

total_2017.columns=['data']
total_2017 = total_2017.reset_index()
total_2017

total_2018.columns=['data']
total_2018 = total_2018.reset_index()
total_2018

total_2019.columns=['data']
total_2019 = total_2019.reset_index()
total_2019

total_2020.columns=['data']
total_2020 = total_2020.reset_index()
total_2020

total_2021.columns=['data']
total_2021 = total_2021.reset_index()
total_2021

# folium 활용하기
import requests
import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import os
import webbrowser
import folium
from folium import plugins
print(folium.__version__)

# 서울시 좌표 파일 가져오기
geo_path = ('./skorea_municipalities_geo_simple - 복사본.json')
geo_str = json.load(open(geo_path, encoding='utf-8'))
geo_str

# 좌표 보여주기
seoul_map = folium.Map(location=[37.5502, 126.982], zoom_start= 10)
seoul_map

## 인스타그램 지도 시각화
folium.Choropleth(
    geo_data = geo_str,
    data = pair_df,
    columns = ['자치구', '맛집'],
    fill_color='PuRd',
    key_on='feature.properties.name',
    fill_opacity=0.8
    ).add_to(seoul_map)

seoul_map

## 네이버 데이터 API 시각화
folium.Choropleth(
    geo_data = geo_str,
    data = df4,
    columns = ['index', '2016'],
    fill_color='PuBuGn',
    key_on='feature.properties.name',
    fill_opacity=0.8
    ).add_to(seoul_map)

seoul_map

## 참고
### [https://choihyuunmin.tistory.com/m/12?category=895651](https://choihyuunmin.tistory.com/m/12?category=895651)

### [https://krksap.tistory.com/1751](https://krksap.tistory.com/1751)



