from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class VariableSet():
    def __init__(self):

        """
        리포트 정보
        """
        self.report_title = 'TestAutomation Result(Sandbox)'
        self.report_title_cbt = 'TestAutomation Result(CBT)'
        self.report_test_evn = 'MAC(11.1)/Chrome(91.0)'

        """
        스프레드시트 정보
        """
        self.spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1Ax3uamNiCwUdl3qE52Fr-ir05XEYw63TDEcYsdMqUPc/edit#gid=0'

        """
        지역정보 타게팅
        데이터 가져오는 방법 : https://wiki.daumkakao.com/pages/viewpage.action?pageId=877167151
        """
        # 지역 정보
        self.region = ['Seoul', 'Gyeonggi']
        # 서울
        self.region_Seoul = {'서울': [{"value":"I1000","description":"서울특별시 강남구","depth1Name":"서울특별시","depth2Name":"강남구"},{"value":"I1001","description":"서울특별시 강동구","depth1Name":"서울특별시","depth2Name":"강동구"},{"value":"I1002","description":"서울특별시 강북구","depth1Name":"서울특별시","depth2Name":"강북구"},{"value":"I1003","description":"서울특별시 강서구","depth1Name":"서울특별시","depth2Name":"강서구"},{"value":"I1004","description":"서울특별시 관악구","depth1Name":"서울특별시","depth2Name":"관악구"},{"value":"I1005","description":"서울특별시 광진구","depth1Name":"서울특별시","depth2Name":"광진구"},{"value":"I1006","description":"서울특별시 구로구","depth1Name":"서울특별시","depth2Name":"구로구"},{"value":"I1007","description":"서울특별시 금천구","depth1Name":"서울특별시","depth2Name":"금천구"},{"value":"I1008","description":"서울특별시 노원구","depth1Name":"서울특별시","depth2Name":"노원구"},{"value":"I1009","description":"서울특별시 도봉구","depth1Name":"서울특별시","depth2Name":"도봉구"},{"value":"I1010","description":"서울특별시 동대문구","depth1Name":"서울특별시","depth2Name":"동대문구"},{"value":"I1011","description":"서울특별시 동작구","depth1Name":"서울특별시","depth2Name":"동작구"},{"value":"I1012","description":"서울특별시 마포구","depth1Name":"서울특별시","depth2Name":"마포구"},{"value":"I1013","description":"서울특별시 서대문구","depth1Name":"서울특별시","depth2Name":"서대문구"},{"value":"I1014","description":"서울특별시 서초구","depth1Name":"서울특별시","depth2Name":"서초구"},{"value":"I1015","description":"서울특별시 성동구","depth1Name":"서울특별시","depth2Name":"성동구"},{"value":"I1016","description":"서울특별시 성북구","depth1Name":"서울특별시","depth2Name":"성북구"},{"value":"I1017","description":"서울특별시 송파구","depth1Name":"서울특별시","depth2Name":"송파구"},{"value":"I1018","description":"서울특별시 양천구","depth1Name":"서울특별시","depth2Name":"양천구"},{"value":"I1019","description":"서울특별시 영등포구","depth1Name":"서울특별시","depth2Name":"영등포구"},{"value":"I1020","description":"서울특별시 용산구","depth1Name":"서울특별시","depth2Name":"용산구"},{"value":"I1021","description":"서울특별시 은평구","depth1Name":"서울특별시","depth2Name":"은평구"},{"value":"I1022","description":"서울특별시 종로구","depth1Name":"서울특별시","depth2Name":"종로구"},{"value":"I1023","description":"서울특별시 중구","depth1Name":"서울특별시","depth2Name":"중구"},{"value":"I1024","description":"서울특별시 중랑구","depth1Name":"서울특별시","depth2Name":"중랑구"}]}
        # 강원도
        self.region_Gangwon = []
        # 경기도
        self.region_Gyeonggi = {'경기': [{"value":"B7200","description":"경기도 가평군","depth1Name":"경기도","depth2Name":"가평군"},{"value":"B4444","description":"경기도 고양시 덕양구","depth1Name":"경기도","depth2Name":"고양시 덕양구"},{"value":"B4433","description":"경기도 고양시 일산동구","depth1Name":"경기도","depth2Name":"고양시 일산동구"},{"value":"B4422","description":"경기도 고양시 일산서구","depth1Name":"경기도","depth2Name":"고양시 일산서구"},{"value":"B7203","description":"경기도 과천시","depth1Name":"경기도","depth2Name":"과천시"},{"value":"B7204","description":"경기도 광명시","depth1Name":"경기도","depth2Name":"광명시"},{"value":"B7205","description":"경기도 광주시","depth1Name":"경기도","depth2Name":"광주시"},{"value":"B7206","description":"경기도 구리시","depth1Name":"경기도","depth2Name":"구리시"},{"value":"B7207","description":"경기도 군포시","depth1Name":"경기도","depth2Name":"군포시"},{"value":"B7208","description":"경기도 김포시","depth1Name":"경기도","depth2Name":"김포시"},{"value":"B7209","description":"경기도 남양주시","depth1Name":"경기도","depth2Name":"남양주시"},{"value":"B7210","description":"경기도 동두천시","depth1Name":"경기도","depth2Name":"동두천시"},{"value":"B2000","description":"경기도 부천시","depth1Name":"경기도","depth2Name":"부천시"},{"value":"B2233","description":"경기도 성남시 분당구","depth1Name":"경기도","depth2Name":"성남시 분당구"},{"value":"B2244","description":"경기도 성남시 수정구","depth1Name":"경기도","depth2Name":"성남시 수정구"},{"value":"B2255","description":"경기도 성남시 중원구","depth1Name":"경기도","depth2Name":"성남시 중원구"},{"value":"B2277","description":"경기도 수원시 권선구","depth1Name":"경기도","depth2Name":"수원시 권선구"},{"value":"B2299","description":"경기도 수원시 영통구","depth1Name":"경기도","depth2Name":"수원시 영통구"},{"value":"B2288","description":"경기도 수원시 장안구","depth1Name":"경기도","depth2Name":"수원시 장안구"},{"value":"B2266","description":"경기도 수원시 팔달구","depth1Name":"경기도","depth2Name":"수원시 팔달구"},{"value":"B7216","description":"경기도 시흥시","depth1Name":"경기도","depth2Name":"시흥시"},{"value":"B7777","description":"경기도 안산시 단원구","depth1Name":"경기도","depth2Name":"안산시 단원구"},{"value":"B7766","description":"경기도 안산시 상록구","depth1Name":"경기도","depth2Name":"안산시 상록구"},{"value":"B7218","description":"경기도 안성시","depth1Name":"경기도","depth2Name":"안성시"},{"value":"B3333","description":"경기도 안양시 동안구","depth1Name":"경기도","depth2Name":"안양시 동안구"},{"value":"B3311","description":"경기도 안양시 만안구","depth1Name":"경기도","depth2Name":"안양시 만안구"},{"value":"B7220","description":"경기도 양주시","depth1Name":"경기도","depth2Name":"양주시"},{"value":"B7221","description":"경기도 양평군","depth1Name":"경기도","depth2Name":"양평군"},{"value":"B7222","description":"경기도 여주시","depth1Name":"경기도","depth2Name":"여주시"},{"value":"B7223","description":"경기도 연천군","depth1Name":"경기도","depth2Name":"연천군"},{"value":"B7224","description":"경기도 오산시","depth1Name":"경기도","depth2Name":"오산시"},{"value":"B7755","description":"경기도 용인시 기흥구","depth1Name":"경기도","depth2Name":"용인시 기흥구"},{"value":"B7733","description":"경기도 용인시 수지구","depth1Name":"경기도","depth2Name":"용인시 수지구"},{"value":"B7744","description":"경기도 용인시 처인구","depth1Name":"경기도","depth2Name":"용인시 처인구"},{"value":"B7227","description":"경기도 의왕시","depth1Name":"경기도","depth2Name":"의왕시"},{"value":"B7228","description":"경기도 의정부시","depth1Name":"경기도","depth2Name":"의정부시"},{"value":"B7229","description":"경기도 이천시","depth1Name":"경기도","depth2Name":"이천시"},{"value":"B7230","description":"경기도 파주시","depth1Name":"경기도","depth2Name":"파주시"},{"value":"B7232","description":"경기도 평택시","depth1Name":"경기도","depth2Name":"평택시"},{"value":"B7233","description":"경기도 포천시","depth1Name":"경기도","depth2Name":"포천시"},{"value":"B7234","description":"경기도 하남시","depth1Name":"경기도","depth2Name":"하남시"},{"value":"B7235","description":"경기도 화성시","depth1Name":"경기도","depth2Name":"화성시"}]}
        # 경상남도
        self.region_Gyeongbuk = []
        # 경상북도
        self.region_Gyeongnam = []
        # 광주광역시
        self.region_Gwangju = []
        # 대구광역시
        self.region_Daegu = []
        # 대전광역시
        self.region_Daejeon = []
        # 부산광역시
        self.region_Busan = []
        # 울산광역시
        self.region_Ulsan = []
        # 인천광역시
        self.region_Incheon = []
        # 전라남도
        self.region_Jeonnam = []
        # 전라북도
        self.region_Jeonbuk = []
        # 제주
        self.region_Jeju = []
        # 충청남도
        self.region_Chungnam = []
        # 충청북도
        self.region_Chungbuk = []
        # 세종
        self.region_Sejong = []