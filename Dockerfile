FROM python:3.7
ADD . /srv/auto-factorial
WORKDIR /srv/auto-factorial
RUN pip install --upgrade pip
RUN pip3 install -r requirements.lock
CMD python3 -m src
