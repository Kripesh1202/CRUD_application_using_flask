FROM python:3

ADD requirement.txt .

RUN pip install -r requirement.txt

ADD app.py .

ADD api.py .

ADD db.py .

CMD ["python", "./app.py"]