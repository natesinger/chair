FROM ubuntu:bionic

WORKDIR /usr/src/app

RUN apt update && apt install python3 python3-pip -y
RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY auth.json ./
COPY run.py ./

CMD [ "python3", "./run.py" ]