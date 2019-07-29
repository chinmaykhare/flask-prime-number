FROM python:3.7-stretch
RUN pip install flask
RUN pip install mysql-connector-python
EXPOSE 9000
CMD ["python","./flask-prime-number/app.py"]