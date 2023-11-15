FROM python:3.10-bullseye

COPY . /

RUN pip3 install -r requirements.txt

CMD [ "python3", "run.py"]