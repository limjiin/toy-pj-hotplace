# Instagram web crawling

# 해시태그 '맛집', '카페' 데이터 각각 1만 건 씩 추출 

# 셀레니움 import
import pandas as pd
import numpy as np

import selenium
from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.parse import quote_plus

import time
from tqdm import tqdm_notebook
import warnings
warnings.filterwarnings('ignore')
import datetime

# 웹페이지  열기
driver = webdriver.Chrome('./chromedriver.exe')
url = f'https://www.instagram.com/'
driver.get(url)

# 검색창에 키워드 입력하기 
tag = '카페'
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(f'{tag}\n')
time.sleep(3)

# 검색창 enter
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]').click()

# 첫번째 게시물 클릭하기
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()

# html
html = BeautifulSoup(driver.page_source, 'html.parser')

# 첫번째 게시물 클릭하기 2번째 방법
def click_first(driver):
    first = driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0')
    first.click()
    time.sleep(3)
click_first(driver)

# 다음 게시글 클릭하기
def next_page(driver):
    next_page = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
    next_page.click()
    time.sleep(3)
next_page(driver)

#크롤링 결과를담을 리스트 생성
result = [ ]

# 여러 게시글 수집하기
target = 1000      # 크롤링할 게시글 수
for i in range(target):

    print(f'{i}번째 게시물 크롤링 중입니다.')

    # 게시글 수집에 오류 발생시 5초 대기후, 다음 게시글로 넘어가도록 예외처리 구문 활용
    try:
        data = get_content(driver)    # 게시글 정보 가져오기
        result.append(data)
        next_page(driver)
    except:
        time.sleep(5)
        next_page(driver)

result = pd.DataFrame(result)
result

# 엑셀 파일에 저장하기
result.to_excel('ins_test.xlsx')








