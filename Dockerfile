FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBYFFERED 1

WORKDIR /code/


RUN pip install pipenv
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
CMD ["python", "main.py"]
