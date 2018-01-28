FROM python:3.6

RUN pip install uwsgi

WORKDIR /collector
ADD ./collector /collector

RUN pip install -r requirements.txt

CMD [ "python3", "webui.py" ]
