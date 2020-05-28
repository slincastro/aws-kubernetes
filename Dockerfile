FROM python:3.6.1-alpine
WORKDIR /project
ADD ./src /project
RUN pip install -r requirements.txt
CMD ["python","service.py"]