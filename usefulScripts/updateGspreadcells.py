import random
from model.data.GoogleDriveAPIAuth import GoogleAPIAuth
from model.data.VariableSet import VariableSet

vs = VariableSet()

# 스프레스시트 문서 가져오기
gd = GoogleAPIAuth()
doc = gd.gc.open_by_url(vs.spreadsheet_url)
ws = doc.worksheet('sheet1')

# 검색 결과를 리스트로 저장하기 위해 results 변수명 지정
results = []

# random 숫자 획득
startrow = 6
count = 10

for i in range(count):
    a = random.randint(1, 3000)
    results.append(a)
    print(results)

cells = ws.range('K' + str(startrow) + ':K' + str(startrow + count))

for i, val in enumerate(results):
    cells[i].value = val

# 리스트값 한 번에 저장
ws.update_cells(cells)