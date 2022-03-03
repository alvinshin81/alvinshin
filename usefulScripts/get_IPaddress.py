from urllib.parse import urlparse
import socket
import pandas as pd
import time

from model.data.GoogleDriveAPIAuth import GoogleAPIAuth as gd
from model.data.VariableSet import VariableSet as vs

# 스프레드시트 데이터 가져오기
doc = gd().gc.open_by_url(vs().spreadsheet_url)
ws = doc.worksheet('시트5')
values = ws.get_all_values()

# 시작할 행 숫자 입력
startrow = 2

# 헤더와 데이터 테이블 범위 지정
header, rows = values[0], values[startrow - 1:]
excel_source = pd.DataFrame(rows)
print("host 개수: " + str(len(excel_source)) + "개")

# 초기 변수 선언
results = []
i = 0


# 메소드 모아놓은 클래스로 이동해도 됨
def get_ip_address(url):
    try:
        up = urlparse(url)
        hostname = up.hostname
        port = up.port or (443 if up.scheme == 'https' else 80)
        ip_addr = socket.getaddrinfo(hostname, port)[0][4][0]
    except:
        ip_addr = "찾기 실패"

    results.append((url, ip_addr))


for data in range(len(excel_source)):
    url = excel_source[1][i]
    if not "https://" in url:
        url = 'https://' + url
    get_ip_address(url)
    i += 1
    time.sleep(1)

# 스프레드시트에 결과 입력
ws.update('C' + str(startrow), results)