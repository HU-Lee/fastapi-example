FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PORT 8000
ENV GUNICORN_CONF /app/app/conf_gunicorn.py
ENV PUBLIC_URL http://openapi.data.go.kr/openapi/service/rest/Covid19

COPY ./requirements.txt .
COPY ./loadbalance-0.0.1-py3-none-any.whl .
RUN pip install -r requirements.txt
RUN pip install loadbalance-0.0.1-py3-none-any.whl 

EXPOSE 8000

COPY ./app /app/app
COPY ./covid /app/covid