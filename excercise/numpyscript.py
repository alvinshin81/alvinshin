import numpy as np
import pandas as pd
from model.data.GoogleDriveAPIAuth import GoogleAPIAuth
from model.data.VariableSet import VariableSet

## 스프레드시트 사용
# 스프레스시트 문서 가져오기
vs = VariableSet()
gd = GoogleAPIAuth()
doc = gd.gc.open_by_url(vs.spreadsheet_url)
ws = doc.worksheet('응답결과')

body = ['1', '3', '8', '15']

print('수험번호를 입력하세요.: ')
ck = input()

result = []
for index, b in enumerate(body):
    judge = np.where(ck == b, 'Pass', 'Fail')
    result.append((b, judge.tolist()))
    if judge == 'Pass':
        break
    ws.update('F2', judge.tolist())

print(result)
print('Final result: ' + str(judge))
