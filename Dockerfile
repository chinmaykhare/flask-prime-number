FROM python:3.8.0b2-alpine3.10
RUN apk add bash
RUN pip install flask
RUN pip install mysql-connector-python
EXPOSE 9000
CMD ["python","./flask-prime-number/app.py"]