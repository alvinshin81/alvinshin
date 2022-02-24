import requests
import pandas as pd
import sys
import os
import random
import time
from datetime import datetime

# 젠킨스 사용 시 활성화 시킬 것
# sys.path.append(os.environ['WORKSPACE']) # jenkins

from model.data.GoogleDriveAPIAuth import GoogleAPIAuth
from model.data.VariableSet import VariableSet


# 스프레드시트 데이터 가져오기
vs = VariableSet()
gd = GoogleAPIAuth()
doc = gd.gc.open_by_url(vs.spreadsheet_url)
ws = doc.worksheet('소재정보')
# doc = gd.gc.open_by_url(vs.spreadsheet_test)
# ws = doc.worksheet('시트1')
values = ws.get_all_values()

# 시작할 행 숫자 입력
startrow = 2

# 헤더와 데이터 테이블 범위 지정
header, rows = values[0], values[startrow - 1:]
excel_source = pd.DataFrame(rows)
print("소재 개수: " + str(len(excel_source)) + "개")
# print(excel_source)

# 초기 변수 선언
results = []
i = startrow
j = 0
number = len(excel_source)
dt = datetime.fromtimestamp(time.time())
date = '빌드날짜 : ' + str(dt)[:16]

def get_excel_source(row):
    # 노출/클릭수량 관련 랜덤값 설정
    rainta = 100  # raintb보다 항상 작게
    raintb = 10000
    diva = 10  # divb보다 항상 작게
    divb = 100

    # # API 고정 변수 지정
    # 건당 과금금액
    chargeAmount_CPM = random.randint(1,3)
    chargeAmount = random.randint(50,300)
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

    # 발송 건수
    msgCount_CPM = random.randint(rainta, raintb)
    a = random.randint(diva, divb)
    msgCount = int(msgCount_CPM / a)

    # 건별 과금 발송 (API Request)
    server = '{서버주소}'
    path = '{URI}'
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
    results.append(
        (representativeId, spendingMethod_CPM, chargeAmount_CPM, msgCount_CPM, response_CPM.status_code, spendingMethod,
         chargeAmount, msgCount, response.status_code))

    return results

# 데이터가 100개가 넘을 경우 100개 단위로 결과값 입력
while number >= 100:
    for data in range(100):
        api_response = get_excel_source(j)
        i += 1
        j += 1
        number -= 1
        time.sleep(1)

    # 스프레드시트에 결과값 일괄 입력
    print("[[" + str(j) + "번째 과금 완료]]")
    ws.update('G' + str(startrow), results)

midrow = j

# 리스트 초기화
results = []

print("[[마지막 소재 개수: " + str(len(excel_source) - j) + "]]")
for data in range(len(excel_source) - j):
    api_response = get_excel_source(j)
    i += 1
    j += 1
    time.sleep(1)

# 스프레드시트에 결과값 일괄 입력
ws.update('G' + str(startrow + midrow), results)

# 스프레드시트에 빌드날짜 입력
ws.update('P1', date)

print("[[" + str(j) + "번째 과금 완료]]")