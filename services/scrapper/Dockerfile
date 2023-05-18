FROM --platform=linux/amd64 python:3.6.4
RUN apt-get update
RUN apt-get install -yqq --no-install-recommends \
    # netcat \
    && apt-get -q clean
RUN apt-get install libpq-dev
RUN mkdir -p /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

ENV FLASK_APP project/__init__.py
ENV APP_SETTINGS project.config.DevelopmentConfig

ENV PORT 5008

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
