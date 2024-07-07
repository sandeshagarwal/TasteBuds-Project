FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure python output is sent directly to thr terminal without buffering
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /usr/src/app/docker-entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]



