FROM python:3.9.10-alpine3.15
WORKDIR /app
COPY requirements.txt ./
RUN apk --no-cache --virtual build-deps add git gcc build-base libffi-dev \
	&& pip install -r requirements.txt \
	&& apk del build-deps
COPY . .
CMD python app/main.py
