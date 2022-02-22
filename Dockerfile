FROM python:3.9.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app/main.py
