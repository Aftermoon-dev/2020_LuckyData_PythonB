from urllib import parse
import requests
import pprint
import xmltodict
import json
import datetime

# 보건복지부_코로나19 감염 현황 (https://data.go.kr/data/15043376/openapi.do)
Covid19_URL = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
Covid19_ServiceKey = ''

nowDate = datetime.datetime.now().strftime('%Y%m%d')

# Parameters - Service Key, Page Number, Page Data 수, 조회 시작 날짜, 조회 종료 날짜
Covid19_Params = {'serviceKey': Covid19_ServiceKey, 'pageNo': '1', 'numOfRows': '1', 'startCreateDt': nowDate, 'endCreateDt': nowDate}

# GET으로 요청
Covid19_Get = requests.get(Covid19_URL, params=Covid19_Params)

# XML Parse
Covid19_Parse = xmltodict.parse(Covid19_Get.text)

if Covid19_Parse['response']['body']['totalCount'] != '0':
    # 각 Item만 가져옴
    Covid19 = Covid19_Parse['response']['body']['items']['item']

    # 출력
    print(Covid19['stateDt'], '코로나19 정보')
    print('검사 진행 수 :', Covid19['examCnt'])
    print('확진자 수 :', Covid19['decideCnt'])
    print('격리 해제 수 :', Covid19['clearCnt'])
    print('사망자 수 :', Covid19['deathCnt'])
else:
    print(nowDate, '일자의 코로나 정보가 아직 존재하지 않습니다. 추후 다시 시도해주세요.')

print('\n')

# 한국환경공단_미세먼지 경보 발령 현황 (https://data.go.kr/data/15034344/openapi.do)
Dust_URL = 'http://openapi.airkorea.or.kr/openapi/services/rest/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
Dust_ServiceKey = ''

# Parameters - Service Key, Page Number, Page Data 수, 조회 년도, 미세먼지 항목 (PM10, PM25) - 모두 가져오려면 공백 or 파라미터 X, Data Type (JSON, XML)
Dust_Params = {'serviceKey': Dust_ServiceKey, 'pageNo': '1', 'numOfRows': '10', 'year': '2020', 'itemCode': '', '_returnType': 'json'}

# GET으로 요청
Dust_Get = requests.get(Dust_URL, params=Dust_Params)

# JSON을 Dict 형태로 변환
Dust = json.loads(Dust_Get.text)['list']

if len(Dust) != 0:
    print('미세먼지 경보 목록')
    for i in range(len(Dust)):
        print('권역 :', Dust[i]['moveName'])
        print('지역 :', Dust[i]['districtName'])
        print('발령 날짜 :', Dust[i]['dataDate'])
        print('발령 시간 :', Dust[i]['issueTime'])
        print('발령 농도 :', Dust[i]['issueVal'])
        print('해제 날짜 :', Dust[i]['clearDate'])
        print('해제 시간 :', Dust[i]['clearTime'])
else:
    print('데이터를 가져올 수 없었습니다. 아직 조회할 수 없는 년도이거나 잘못된 년도일 수 있습니다.')