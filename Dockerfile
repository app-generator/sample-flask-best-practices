FROM python:3.10.4-slim-bullseye
LABEL maintainer="Chirilov Adrian<chirilov.adrian@gmail.com>"

COPY . /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python" ,"run.py"]
EXPOSE 5000