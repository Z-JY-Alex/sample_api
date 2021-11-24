FROM python:3.6

WORKDIR /sample_api

COPY ./requirements.txt /sample_api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /apiservice/requirements.txt

COPY ./app /sample_api/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
