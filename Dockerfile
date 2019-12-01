FROM python:3.7

RUN mkdir -p /service
WORKDIR /service
COPY ./ /service/

RUN pip3 install -r requirements.txt

CMD ["sh", "start.sh"]