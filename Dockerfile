FROM python:3.6.7

COPY ./requirements.txt /tradutor/

WORKDIR /tradutor

EXPOSE 3000

RUN pip install -r requirements.txt

COPY ./src/ /tradutor/

CMD ["python", "/tradutor/app.py"]