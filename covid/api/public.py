from covid.database.crud import create_or_update_inter, create_or_update_korea
from sqlalchemy.orm.session import Session
from covid.util import get_before_day
import os
import requests
import xmltodict
from dotenv import load_dotenv

load_dotenv(verbose=True)

PUBLIC_KEY = os.getenv("PUBLIC_KEY")
PUBLIC_URL = os.getenv("PUBLIC_URL")

# 오늘의 국내 코로나 정보
# 간단히 업데이트 날짜, 오늘 확진자 수, 오늘 사망자 수만 저장
def save_korea(db: Session, before:int=0) -> None:
    after = get_before_day(0 + before, "%Y%m%d")
    before = get_before_day(2 + before, "%Y%m%d")
    url = "{}/getCovid19InfStateJson?serviceKey={}&startCreateDt={}&endCreateDT={}".format(PUBLIC_URL, PUBLIC_KEY, before, after)
    raw = requests.get(url).text.encode('utf-8')
    data = xmltodict.parse(raw)['response']['body']['items']["item"]
    date = data[0]["stateDt"]
    detected = int(data[0]["decideCnt"]) - int(data[1]["decideCnt"])
    death = int(data[0]["deathCnt"]) - int(data[1]["deathCnt"])
    print(date, detected, death)
    # DB 저장
    create_or_update_korea(db, date, detected, death)

# 국제 코로나 정보
# 간단히 일본, 미국의 확진자만 저장
def save_jpus(db: Session, before:int=0) -> None:
    after = get_before_day(0 + before, "%Y%m%d")
    before = get_before_day(2 + before, "%Y%m%d")
    url = "{}/getCovid19NatInfStateJson?serviceKey={}&startCreateDt={}&endCreateDT={}".format(PUBLIC_URL, PUBLIC_KEY, before, after)
    raw = requests.get(url).text.encode('utf-8')
    data = xmltodict.parse(raw)['response']['body']['items']["item"]
    date = data[0]["createDt"][:10].replace("-","")
    dic = {}
    for i in ["일본", "미국"]:
        con_data = list(filter(lambda x: x["nationNm"]==i, data))
        dic[i] = int(con_data[0]["natDefCnt"]) - int(con_data[1]["natDefCnt"])
    print(date, dic["일본"], dic["미국"])
    # DB 저장
    create_or_update_inter(db, date, dic["일본"], dic["미국"])