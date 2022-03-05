import time
import requests
import random
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import os


class Utility():
    def __init__(self, driver={}):
        self.driver = driver

    def click_id_after_webDriverWait(self, driver, id, timeout=10):
        """
        id 값에 해당하는 element 클릭
        :param driver: 사용 드라이버
        :param id: element id
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, id))).click()

    def click_classname_after_webDriverWait(self, driver, classname, timeout=10):
        """
        id 값에 해당하는 element 클릭
        :param driver: 사용 드라이버
        :param classname: element class name
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, classname))).click()

    def click_xpath_after_webDriverWait(self, driver, xpath, timeout=10):
        """
        xpath 값에 해당하는 element 클릭
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()

    def click_cssSelector_after_webDriverWait(self, driver, cssSelector, timeout=10):
        """
        xpath 값에 해당하는 element 클릭
        :param driver: 사용 드라이버
        :param cssSelector: element cssSelector
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector))).click()

    def click_linktext_after_webDriverWait(self, driver, linktext, timeout=10):
        """
        xpath 값에 해당하는 element 클릭
        :param driver: 사용 드라이버
        :param linktext: element link text
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.LINK_TEXT, linktext))).click()

    def click_xpath_after_webDriverWait_clickable(self, driver, xpath, timeout=10):
        """
        xpath 값에 해당하는 element 클릭
        :param driver: 사용 드라이버
        :param linktext: element link text
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def getText_xpath_after_webDriverWait(self, driver, xpath, timeout=10):
        """
        xpath 값에 해당하는 element의 text 추출
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :param timeout: 대기시간(s)
        :return: -
        """
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element.text

    def getText_css_after_webDriverWait(self, driver, css, timeout=10):
        """
        xpath 값에 해당하는 element의 text 추출
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :param timeout: 대기시간(s)
        :return: -
        """
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return element.text

    def getText_classname_after_webDriverWait(self, driver, classname, timeout=10):
        """
        name 값에 해당하는 element의 text 추출
        :param driver: 사용 드라이버
        :param classname: element class name
        :param timeout: 대기시간(s)
        :return: element text
        """
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, classname)))
        return element.text

    def setText_xpath_after_webDriverWait(self, driver, xpath, text, timeout=10):
        """
        xpath 값에 해당하는 element에 문자열 입력
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :param text: 입력하고자하는 문자열
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(text)

    def setText_name_after_webDriverWait(self, driver, className, text, timeout=10):
        """
        name 값에 해당하는 element에 문자열 입력
        :param driver: 사용 드라이버
        :param className: element class name
        :param text: 입력하고자하는 문자열
        :param timeout: 대기시간(s)
        :return: -
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, className))).send_keys(
            text)

    def setText_id_after_webDriverWait(self, driver, id, text, timeout=10):
        """
        id 값에 해당하는 element에 문자열 입력
        :param driver: 사용 드라이버
        :param id: element id
        :param text: 입력하고자하는 문자열
        :param timeout: 대기시간(s)
        :return:
        """
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, id))).send_keys(text)
        time.sleep(1)

    def setBP_xpath_after_webDriverWait(self, driver, xpath, size=100, timeout=20):
        """
        xpath 값에 해당하는 element에 BACKSPACE 입력 (지우기)
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :param size: 지우고자하는 크기(디폴트 100자)
        :param timeout: 대기시간(s)
        :return: -
        """
        for i in range(size):
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(
                Keys.BACKSPACE)

    def upload_xpath_after_webDriverWait(self, driver, xpath, src, timeout=10):
        """
        xpath 값에 해당하는 element에 파일 업로드
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :param src: 파일 디렉토리 위치(img, video, ...)
        :param timeout: 대기시간(s)
        :return: -
        """
        absolute_path = os.path.abspath(src)
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(
            absolute_path)

    # 마우스오버
    def hoverAndclick(self, driver, hover_xpath, click_xpath):
        """
        마우스 오버 이후 클릭까지 연속 동작
        :param driver: 사용 드라이버
        :param hover_xpath: 마우스 오버할 대상 xpath
        :param click_xpath: 마우스 오버 이후 클릭할 대상 xpath
        :return: -
        """
        a = ActionChains(driver)

        m = driver.find_element_by_xpath(hover_xpath)
        a.move_to_element(m).perform()

        n = driver.find_element_by_xpath(click_xpath)
        a.move_to_element(n).click().perform()

    def is_displayed_xpath(self, driver, xpath):
        """
        xpath 값에 해당하는 element가 노출되는지 판별
        :param driver: 사용 드라이버
        :param xpath: element xpath
        :return: boolean
        """
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    # 스크롤 관련 메소드
    def scroll_down(self, height=0):
        """
        웹 페이지 scroll down
        :param height: 수행할 Scroll 높이값 (입력안하면 최하단으로 scroll down)
        :return: -
        """
        if height == 0:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        else:
            self.driver.execute_script("window.scrollTo(0, window.scrollY + " + str(height) + ");")
            time.sleep(1)

    def scroll_up(self, height=0):
        """
        웹 페이지 scroll up
        :param height: 수행할 Scroll 높이값
        :return: -
        """
        self.driver.execute_script("scrollBy(0,-" + str(height) + ");")
        time.sleep(1)

    def back(self):
        self.driver.back()
        time.sleep(2)

    def forward(self):
        self.driver.forward()
        time.sleep(2)

    def switch_to_new_window(self):
        """
        func : 드라이버 새 창으로 이동 (창 2개 노출상태에서 2번째로 이동)
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)

    def close_window_and_switch_to_before_window(self):
        """
        func : 드라이버 현재 창 닫고, 이전 창으로 이동 (창 2개 노출상태에서 1번째로 이동)
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

    def close_window_and_switch_to_before_window1(self):
        """
        func : 드라이버 현재 창 닫고, 이전 창으로 이동 (창 3개 노출상태에서 2번째로 이동)
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    # def getNumber_cssSelector_after_webDriverWait(self, driver, query):
    #     """
    #     func : 검색 결과 개수 세기
    #     """
    #     self.driver.find_elements_by_css_selector(query)
    #
    def getNumber_cssSelector_after_webDriverWait(self, driver, css, timeout=10):
        """
        func : 검색 결과 개수 세기
        """
        ss = WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
        return ss

    def getText_css_after_webDriverWait(self, driver, css, timeout=10):
        """
        name 값에 해당하는 element의 text 추출
        :param driver: 사용 드라이버
        :param classname: element class name
        :param timeout: 대기시간(s)
        :return: element text
        """
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return element.text


class sprintUtility():
    def sendKakaoTalk(self, msg, groupId):
        server = 'http://api.noti.daumkakao.io/send/group/kakaotalk'
        reqBody = {"to": groupId, "msg": msg}
        data = {
            # 'requestBody': reqBody,
            'contentType': 'APPLICATION_JSON_UTF8'
        }
        response = requests.post(server, params=reqBody, data=data)
        print('카톡전송 상태:' + str(response.status_code))
        # print(response.content)

    def charging_via_API(self, excel_source, row, result):
        # 노출/클릭수량 관련 랜덤값 설정
        rainta = 100  # raintb보다 항상 작게
        raintb = 10000
        diva = 10  # divb보다 항상 작게
        divb = 100

        # # API 고정 변수 지정
        # 건당 과금금액
        chargeAmount_CPM = random.randint(1, 3)
        chargeAmount = random.randint(50, 300)
        # 서버 환경. 샌박 Only 지원으로 건들지 말 것
        profileServer = 'SANDBOX'
        # 과금 방식. CPMS/CPT, 스폰서드 미지원
        spendingMethod_CPM = 'CPM'
        spendingMethod = 'CPC'
        # 테스트 회차
        testDegree = 1

        # 광고계정 ~ 소재ID 추출
        walletId = excel_source[0][row]
        campaignId = excel_source[1][row]
        adGroupId = excel_source[2][row]
        representativeId = excel_source[3][row]
        spendingMethod_org = excel_source[4][row]

        # 발송 건수
        msgCount_CPM = random.randint(rainta, raintb)
        a = random.randint(diva, divb)
        msgCount = int(msgCount_CPM / a)

        if spendingMethod_org == 'CPM':
            chargeAmount = 0
        elif spendingMethod_org == 'CPA':
            spendingMethod = spendingMethod_org
            chargeAmount_CPM = 0
            chargeAmount = 1500
        elif spendingMethod_org == 'CPC':
            chargeAmount_CPM = 0
        elif spendingMethod_org == 'CPV':
            spendingMethod = spendingMethod_org
            chargeAmount_CPM = 0
            chargeAmount = 20
        elif spendingMethod_org == '자동':
            randomAmount = random.choice([0, int(chargeAmount)])
            if randomAmount == 0:
                chargeAmount = randomAmount
            else:
                chargeAmount = 0
        else:
            chargeAmount_CPM = 0
            chargeAmount = 0
            msgCount_CPM = 0
            msgCount = 0

        # 건별 과금 발송 (API Request)
        server = 'http://billing-api-sandbox.moment.devel.kakao.com:8080'
        path = '/qa/cpm_cpc_cpa_cpms'
        params_CPM = {'walletId': walletId, 'adGroupId': adGroupId, 'campaignId': campaignId,
                      'representativeId': representativeId, 'chargeAmount': chargeAmount_CPM, 'msgCount': msgCount_CPM,
                      'profile': profileServer, 'spendingMethod': spendingMethod_CPM, 'testDegree': testDegree}
        time.sleep(1)
        params = {'walletId': walletId, 'adGroupId': adGroupId, 'campaignId': campaignId,
                  'representativeId': representativeId, 'chargeAmount': chargeAmount, 'msgCount': msgCount,
                  'profile': profileServer, 'spendingMethod': spendingMethod, 'testDegree': testDegree}
        url = server + path

        # 응답결과 추출
        response_CPM = requests.post(url, params=params_CPM)
        response = requests.post(url, params=params)
        result.append(
            (representativeId, spendingMethod_CPM, chargeAmount_CPM, msgCount_CPM, response_CPM.status_code,
             spendingMethod,
             chargeAmount, msgCount, response.status_code))

        return result

    def method_test(self, a, b):
        result = a * b
        return result