FROM python:3.10.4-buster
RUN apt-get update
RUN apt-get install -y --no-install-recommends libatlas-base-dev gfortran
LABEL maintainer="Chirilov Adrian<chirilov.adrian@gmail.com>"

COPY . /
WORKDIR /
RUN pip install -r requirements.txt
RUN pip install uwsgi
# CMD [ "python", "run.py"]
CMD [ "uwsgi", "--socket", "0.0.0.0:5000", "--protocol", "http", "--wsgi", "run:app" ]