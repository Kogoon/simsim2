FROM python:3.9.12-slim

WORKDIR /home/

RUN git clone https://github.com/Kogoon/simsim2.git

WORKDIR /home/simsim2/mysite/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=" > .env

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
