FROM python:3.7-slim

WORKDIR /app
COPY requirement.txt .

RUN pip install -r requirement.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY . .

EXPOSE 8080

CMD [ "python3", "app.py" ]