FROM python:3.9

WORKDIR /app

COPY ./Pipfile.lock /app/Pipfile.lock

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv sync

COPY ./main.py /app/
COPY ./svm.ml /app/

EXPOSE 8000
CMD ["pipenv",  "run",  "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]