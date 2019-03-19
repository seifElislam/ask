FROM python:3.5

RUN apt-get update
#RUN apt-get install -y libssl-dev
#RUN apt-get install -y python3-dev python3-pip
#RUN apt-get install -y build-essential python3-mysqldb git vim default-libmysqlclient-dev

COPY ./requirements /requirements
RUN pip install -r /requirements/base_requirements.txt

COPY ./docker/start /start
RUN chmod +x /start

RUN mkdir -p /app
WORKDIR app
