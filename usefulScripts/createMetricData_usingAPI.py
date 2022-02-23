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

vs = VariableSet()

# 스프레드시트 데이터 가져오기
gd = GoogleAPIAuth()
doc = gd.gc.open_by_url(vs.spreadsheet_url)
# ws = doc.worksheet('소재정보')
ws = doc.worksheet('소재정보')
values = ws.get_all_values()

# 시작할 행 숫자 입력
startrow = 2

# 헤더와 데이터 테이블 범위 지정
header, rows = values[0], values[startrow - 1:]
excel_source = pd.DataFrame(rows)
print("소재 개수: " + str(len(excel_source)) + "개")

# 초기 변수 선언
results = []
i = startrow
number = len(excel_source)
j = 0
dt = datetime.fromtimestamp(time.time())
date = '빌드날짜 : ' + str(dt)[:16]
rainta = 100 # raintb보다 항상 작게
raintb = 10000
diva = 10 # divb보다 항상 작게
divb = 100


# # API 고정 변수 지정
# 건당 과금금액
# chargeAmount = 0
# # chargeAmount_CPC = 200
# chargeAmount_CPC = 20
# 서버 환경. 샌박 Only 지원으로 건들지 말 것
profileServer = 'SANDBOX'
# 과금 방식. CPM/CPC만 지원 (CPM: 노출수, CPC: 클릭수)
spendingMethod_CPM = 'CPM'
# 테스트 회차
testDegree = 1

# 데이터가 100개가 넘을 경우 100개 단위로 결과값 입력
while number >= 100:
    for data in range(100):
        # 데이터에서 필요한 변수 취합 (광고계정ID ~ 소재 ID)
        walletId = ws.acell('A' + str(i)).value
        campaignId = ws.acell('B' + str(i)).value
        adGroupId = ws.acell('C' + str(i)).value
        representativeId = ws.acell('D' + str(i)).value
        spendingMethod_org = ws.acell('E' + str(i)).value

        if spendingMethod_org == 'CPM':
            spendingMethod = 'CPC'
            chargeAmount_CPM = 3
            chargeAmount = 0
        elif spendingMethod_org == 'CPA':
            spendingMethod = spendingMethod_org
            chargeAmount_CPM = 0
            chargeAmount = 1500
        elif spendingMethod_org == 'CPC':
            spendingMethod = spendingMethod_org
            chargeAmount_CPM = 0
            chargeAmount = 200
        elif spendingMethod_org == 'CPV':
            spendingMethod = spendingMethod_org
            chargeAmount_CPM = 0
            chargeAmount = 20
        elif spendingMethod_org == '자동':
            spendingMethod = "CPC"
            chargeAmount_CPM = 3
            chargeAmount = 0
        else:
            spendingMethod = "CPC"
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
        results.append((spendingMethod_CPM, chargeAmount_CPM, msgCount_CPM, response_CPM.status_code, spendingMethod,
                        chargeAmount, msgCount, response.status_code))

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
    # 데이터에서 필요한 변수 취합 (광고계정ID ~ 소재 ID)
    walletId = ws.acell('A' + str(i)).value
    campaignId = ws.acell('B' + str(i)).value
    adGroupId = ws.acell('C' + str(i)).value
    representativeId = ws.acell('D' + str(i)).value
    spendingMethod_org = ws.acell('E' + str(i)).value
    if spendingMethod_org == 'CPM':
        spendingMethod = 'CPC'
        chargeAmount_CPM = 3
        chargeAmount = 0
    elif spendingMethod_org == 'CPA':
        spendingMethod = spendingMethod_org
        chargeAmount_CPM = 0
        chargeAmount = 1500
    elif spendingMethod_org == 'CPC':
        spendingMethod = spendingMethod_org
        chargeAmount_CPM = 0
        chargeAmount = 200
    elif spendingMethod_org == 'CPV':
        spendingMethod = spendingMethod_org
        chargeAmount_CPM = 0
        chargeAmount = 20
    elif spendingMethod_org == '자동':
        spendingMethod = "CPC"
        chargeAmount_CPM = 3
        chargeAmount = 0
    else:
        spendingMethod = "CPC"
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
    results.append((spendingMethod_CPM, chargeAmount_CPM, msgCount_CPM, response_CPM.status_code, spendingMethod,
                    chargeAmount, msgCount, response.status_code))

    i += 1
    j += 1
    time.sleep(1)

# 스프레드시트에 결과값 일괄 입력
ws.update('G' + str(startrow + midrow), results)

# 스프레드시트에 빌드날짜 입력
ws.update('O1', date)

print("[[" + str(j) + "번째 과금 완료]]")