FROM python:3.11-rc-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run.py ./

CMD [ "python3", "./run.py" ]