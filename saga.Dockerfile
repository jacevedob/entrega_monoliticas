FROM python:3.10.7

COPY terceros-requirements.txt ./
RUN pip install --no-cache-dir -r terceros-requirements.txt

COPY . .

CMD [ "python", "./entregasalpes/coordinador_saga/main.py" ]