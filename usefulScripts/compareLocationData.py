# -*- coding: utf8 -*-
import time

import pandas as pd
from model.data.GoogleDriveAPIAuth import GoogleAPIAuth
from model.data.VariableSet import VariableSet
vs = VariableSet()

# 비교 지역 선정 (서울 ~ 제주)
target = [vs.region_Gyeonggi, vs.region_Seoul]

## 스프레드시트 사용
# 스프레스시트 문서 가져오기
gd = GoogleAPIAuth()
doc = gd.gc.open_by_url(vs.spreadsheet_url)
ws = doc.worksheet('응답결과')

# 기존 입력값 이후 셀부터 결과 입력하도록 설정
values = ws.get_all_values()
header, rows = values[0], values[1:]
excel_source = pd.DataFrame(rows, columns=header)
print('기존 입력셀 개수: ' + str(len(excel_source)))
# 시작하는 셀 설정
start = len(excel_source)

results = []
# print(target)

for region in target:
    for city in region:
        for area, result in region.items():
            print("지역: " + area)
            print("지역 내 검색 결과: " + str(len(result)))
            i = 0
            for data in range(len(result) ):
                # 지역 및 코드를 스프레드시트에 입력
                for category, output in result[i].items():
                    if category == 'value':
                        lcode = output
                    if category == 'description':
                        location = output
                        i += 1
                        # 검색 결과를 리스트 자료형으로 저장
                        results.append((lcode, location))
                        break
            # 전체 목록을 한번에 저장
            ws.update('A' + str(start + 2), results)
