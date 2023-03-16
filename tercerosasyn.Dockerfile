FROM python:3.10

COPY requirementsTerceros.txt ./
RUN pip install --no-cache-dir -r requirementsTerceros.txt

COPY ./tercerosasyn/ ./tercerosasyn
COPY .env .

CMD [ "uvicorn", "tercerosasyn.main:app" ]
#CMD [ "ls" ]