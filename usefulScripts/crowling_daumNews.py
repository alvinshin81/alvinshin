# Create adAccounts

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl

#환경 설정
url = 'https://news.daum.net/ranking/popular/sports'
folder_name = 'daum'
excel_name = 'news'


driver = webdriver.Chrome('../Driver/chromedriver_93')
driver.implicitly_wait(3)
# driver.maximize_window()

# 웹페이지 진입
driver.get(url)




# 뉴스 요소  찾기
news = driver.find_elements_by_css_selector('ul.list_news2 > li')

# print(reply)
## ul 태그 하위 li 태그 개수 추출
print(len(news))
#


## 작성자와 댓글 내용 추출 (작성자, 댓글내용)
print("[댓글 내용 수집]")
results = []
keyword_results = [] # (index, author, content)
for index, content in enumerate(news) :
    cp = content.find_element_by_css_selector('span.info_news').text
    subject = content.find_element_by_css_selector('a.link_txt').text
    results.append((cp,subject))

pprint((results))


#
## 폴더 생성
# print("[폴더 생성]")
if not os.path.isdir('./{}'.format(folder_name)):
    os.mkdir('./{}'.format(folder_name))

# 엑셀로 저장
print("[전체 댓글 엑셀로 저장]")
import pandas as pd   ## pandas를 pd로 별칭 만들기
col = ["작성자", "내용"]
data_frame = pd.DataFrame(results, columns=col)  ## 어떤 데이터 내용으로 만들것인지 정의
data_frame.to_excel('./{0}/{1}.xlsx'.format(folder_name,excel_name), sheet_name='수집시트명',startrow=0,header=True)

context = ssl._create_unverified_context()
image = urllib.request.urlopen(url, context=context).read()
get_image = BeautifulSoup(image, 'html.parser')
thumbs = get_image.find_all(class_='thumb_g')

if not os.path.isdir('./{0}/{1}'.format(folder_name, 'images')):
    os.mkdir('./{0}/images'.format(folder_name))

for index, thumb in enumerate(thumbs) :
    img = thumb['src']
    with urllib.request.urlopen(img, context=context) as file:
        with open('./{0}/images/'.format(folder_name) + folder_name + '_' + excel_name + str(index) + '.png', 'wb') as b:
            data = file.read()
            b.write(data)

# image = urllib.request.urlopen(url2).read()
# get_image = BeautifulSoup(image, 'html.parser')
# thumb = get_image.find_all(class_='_image')
# print(thumb)



time.sleep(3)
driver.quit()

# 테스트
