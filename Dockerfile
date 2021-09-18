FROM python:3.8

COPY ./requirements/requirements.txt ./requirements/requirements.txt

RUN pip3 install -r requirements/requirements.txt

COPY ./api /api/api

ENV PYTHONPATH=/api
WORKDIR /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["api.main:app", "--host", "0.0.0.0", "--port", "8000"]