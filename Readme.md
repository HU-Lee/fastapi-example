# FastAPI Example

## Todo Before Run
0. requirements.txt의 의존성 설치
1. 공공API 활용신청   
다음 링크에서 활용신청을 하고 API KEY를 발급

https://www.data.go.kr/data/15043376/openapi.do   
https://www.data.go.kr/data/15043379/openapi.do

2. .env 파일 설정
- PUBLIC_KEY
- PUBLIC_URL = http://openapi.data.go.kr/openapi/service/rest/Covid19
- POSTGRES_PASSWORD
- POSTGRES_URL   
`postgresql+psycopg2://postgres:{비번}@{host}:{port}/{db이름}`

host는 로컬 환경에서는 localhost or 127.0.0.1   
docker-compose에서는 서비스 이름이 된다. (여기서는 postgres)



<br/>

## Run on Windows
1. DB 설정
2. 루트 폴더의 win.py 실행

## Run on Docker
gunicorn + docker-compose 이용

1. `docker-compose build --pull`
2. `docker-compose up postgres -d`
3. postgres container의 CLI에 접속하여 covid.sql의 내용을 실행시킴
4. `docker-compose up fastapi -d`


<br/>

## 구현된 기능
- 코로나 공공API 호출 + postgres에 저장
- Simple LB
- Simple graphQL
- uvicorn & gunicorn logging
- Dockerfile
- loadbalance Packaging

## 기타
1. Powershell에서 venv 실행이 안 될 경우   
Powershell 관리자 모드에서 다음을 입력해서 제한을 풀어 준다.   
(보안이 걱정되면 cmd로 경로를 직접 입력해 실행)
```
Set-ExecutionPolicy RemoteSigned
```