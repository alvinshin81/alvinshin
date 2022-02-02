import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib3

# 구글스프레드시트 사용을 위한 인증키
# https://console.cloud.google.com/apis/dashboard?project=kakaoadplatformqa 에서 json 파일 다운로드 완료 (앨빈에게 문의)

class GoogleAPIAuth():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    try:
        json_file_name = '../model/data/GoogleDriveAPI_notupload.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    except:
        json_file_name = './model/data/GoogleDriveAPI_notupload.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)

    def __init__(self):
        self.gc = gspread.authorize(self.credentials)