# Create adAccounts

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

#URL 설정
url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0011981981&m_view=1"

# URL에 댓글보기인 &m_view=1가 없으면 붙여주기
if not '&m_view=1' in url:
    url += '&m_view=1'


driver: WebDriver = webdriver.Chrome('../Driver/chromedriver')
driver.implicitly_wait(3)
# driver.maximize_window()

# 웹페이지 진입
print("[접속하기]")
driver.get(url)


# 더보기 버튼 누르기
print("[더보기 클릭]")
attempt = 0  # 더보기 탐색 횟수
while True:
    try:
        driver.find_element_by_css_selector('span.u_cbox_page_more').click()  #더보기 버튼에 대한 요소를 찾아서 클릭
        attempt = 0
    except:
        attempt += 1
        if attempt > 5:
            print("더보기 버튼 없음")
            break  # 5회 시도 횟수 초과는 더이상 더보기 버튼이 없다라고 생각하겠다.


# 댓글 요소 찾기
print("[댓글 요소 찾기]")
replys = driver.find_elements_by_css_selector('ul.u_cbox_list > li.u_cbox_comment')
## ul 태그 하위 li 태그 개수 추출
print(len(replys))
#
# 작성자 : u_cbox_info_main, 댓글내용 : u_cbox_contents
## 작성자와 댓글 내용 추출 (작성자, 댓글내용)
print("[댓글 내용 수집]")
results = []
keyword_results = [] # (index, author, content)
del_msg = 0
for index, reply in enumerate(replys) :
    try:
        author = reply.find_element_by_css_selector('span.u_cbox_info_main').text ## span에 u_cbox_info_main 태그에 있는 text 를 author로 지정
        content = reply.find_element_by_css_selector('span.u_cbox_contents').text
        results.append((author,content))
    except:
        del_msg += 1  #삭제된 댓글 카운트
#
# print("삭제된 댓글 개수 : ", del_msg)
# pprint((results))
#
# ## 폴더 생성
# print("[폴더 생성]")
import os
folder_name = keyword
if not os.path.isdir('./{}'.format(folder_name)):
    os.mkdir('./{}'.format(folder_name))

##캡쳐
# for index, k in enumerate(keyword_results):
#    replys[k[0]].screenshot('./{0}/{0}{1}.png').format(keyword,index))
#
## 엑셀파일 만들기 (excelscore, pandas를 설정 > Python Interpreter 에 설치해야함)

print("[전체 댓글 엑셀로 저장]")
import pandas as pd   ## pandas를 pd로 별칭 만들기
col = ["작성자", "내용"]
data_frame = pd.DataFrame(results, columns=col)  ## 어떤 데이터 내용으로 만들것인지 정의
data_frame.to_excel('./{0}/{1}.xlsx'.format(keyword,excel_name), sheet_name='수집시트명',startrow=0,header=True)
#

time.sleep(3)
driver.quit()

# 테스트
