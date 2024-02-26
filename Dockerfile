FROM python:3.10.12-alpine3.18

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5001

CMD [ "python", "api/index.py", "--host=0.0.0.0"]