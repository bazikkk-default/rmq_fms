FROM python:3

WORKDIR /opt/fms_agreement

COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

COPY . .

CMD [ "python", "./consumer.py" ]