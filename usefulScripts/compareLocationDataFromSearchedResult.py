import unittest
from functools import wraps
from unittest import TestLoader
import time
import pandas as pd
import openpyxl
from datetime import datetime
import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sys
import urllib3

# 젠킨스 사용 시 활성화 시킬 것
sys.path.append(os.environ['WORKSPACE']) # jenkins


from controller.pageObjects.LoginPage import LoginPage
from controller.pageObjects.KamoDashboard import KamoDashboard
from controller.pageObjects.AdGroupComponent import AdGroupComponent
from controller.pageObjects.ModifyAdGroup import ModifyAdGroup
from controller.pageObjects.CreateAds import CreateAds
from controller.pageObjects.KafobiDashboard import KafobiDashboard
from controller.util.Utility import Utility
from model.data.VariableSet import VariableSet
from controller.pageObjects.adGroup_location import AdGroup_location
from controller.pageObjects.AdGroupComponent import AdGroupComponent
from model.data.GoogleDriveAPIAuth import GoogleAPIAuth
import numpy as np
from model.data.VariableSet import VariableSet

#젠킨스 세팅
vs = VariableSet()

# jenkinsOption_driver1 = True  # jenkinsSetting : True / Local : False
jenkinsOption_driver1 = True  # jenkinsSetting : True / Local : False
jenkinsOption_driver2 = None  # Default : None / jenkinsSetting : True / Local : False / 미사용 : None

driver, driver2 = vs.jenkinsSetting(jenkinsOption_driver1, jenkinsOption_driver2)

driver.get(vs.baseURL)
driver.set_window_rect(1, 1, 1800, 1300)

lp = LoginPage(driver)
lp.setUserName(vs.username_alvin)
lp.setPassword(vs.password_alvin)
lp.clickLogin()

driver.get(vs.alvinURL)
time.sleep(5)

# 광고만들기 > 광고그룹설정 진입
km = KamoDashboard(driver)
km.clickCreateAd()

# 광고 유형/목표
ca = CreateAds(driver)
ca.clickDisplay()
ca.clickVisit()
util = Utility(driver)
util.scroll_down()
ca.clickCreateCampaign()
ca.clickCreateAdGroup()

# 집행 대상 설정
area = AdGroup_location(driver)
btn = AdGroupComponent(driver)
area.clickArea()
area.clickAreaSearch()

# 스프레스시트 문서 가져오기
gd = GoogleAPIAuth()
doc = gd.gc.open_by_url(vs.spreadsheet_url)
# ws = doc.worksheet('동단위_네트워크응답결과')
ws = doc.worksheet('[DA2202A_2] 동 단위 타게팅 정합성테스트')

# # 행 개수 세기
# startrow = 결과 입력 시작할 행
startrow = 2306
values = ws.get_all_values()

# index는 0부터 시작이기 때문에 startrow에서 -1을 해줌
header, rows = values[0], values[startrow - 1:]

# start row 설정 시 헤더값 제외
excel_source = pd.DataFrame(rows)
# excel_source = pd.DataFrame(rows, columns=header)
print("검색어: " + str(len(excel_source)) + "개")

# 검색 결과를 리스트로 저장하기 위해 results 변수명 지정
results = []

# 중간에 멈추면 i값만 변경 (기입력값 개수 = i)
i = startrow
j = 0
number = len(excel_source)

while number >= 100:
    for data in range(1, 101):
        # print("[" + str(i) + '번째 쿼리]')
        # 검색어 입력 (Description 기준)
        query = ws.acell('F' + str(i)).value
        area.queryAreaSearch(query)
        # print("검색어 : " + query)
        btn.clickSearchTargetPopup()
        # 검색 결과 추출 + 특정 문자 제거
        try:
            # 지역 코드 기반 읍면동 검색
            code = ws.acell('C' + str(i)).value
            value = driver.find_element_by_xpath("//*[@for='" + str(code) + "']/ancestor::span").text
            # print("검색결과 : " + value)
            # 결과 판정
            judge = np.where(query == value, "Pass", "Fail")
            # print(judge)
            results.append((query, code, judge.tolist()))
            btn.clickDeleteQueryPopup()
        except:
            results.append((query, "검색 안됨", "Fail"))
            # 검색 필드 초기화
            btn.clickDeleteQueryPopup()
            area.queryAreaSearch("test")
            btn.clickDeleteQueryPopup()
        i += 1
    number -= 100
    j += 100
    print("[[" + str(j) + "번째 검색 완료]]")

    # 전체 목록을 한번에 저장
    ws.update('H' + str(startrow), results)


for data in range(len(excel_source) - j):
    # print("[" + str(i) + '번째 쿼리]')
    # 검색어 입력 (Description 기준)
    query = ws.acell('F' + str(i)).value
    area.queryAreaSearch(query)
    # print("검색어 : " + query)
    btn.clickSearchTargetPopup()
    # 검색 결과 추출 + 특정 문자 제거
    try:
        # 지역 코드 기반 읍면동 검색
        code = ws.acell('C' + str(i)).value
        value = driver.find_element_by_xpath("//*[@for='" + str(code) +"']/ancestor::span").text
        # print("검색결과 : " + value)
        # 결과 판정
        judge = np.where(query == value, "Pass", "Fail")
        # print(judge)
        results.append((query, code, judge.tolist()))
        btn.clickDeleteQueryPopup()
    except:
        results.append((query, "검색 안됨", "Fail"))
        #검색 필드 초기화
        btn.clickDeleteQueryPopup()
        area.queryAreaSearch("test")
        btn.clickDeleteQueryPopup()
    i += 1
    j += 1

# 전체 목록을 한번에 저장
ws.update('H' + str(startrow), results)
print("[[" + str(j) + "번째 검색 완료]]")


time.sleep(3)
driver.quit()