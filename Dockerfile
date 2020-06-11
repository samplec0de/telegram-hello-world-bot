FROM python:3.8
ENV LC_ALL C.UTF-8

WORKDIR /usr/src/app

COPY requirements.txt bot.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "./bot.py"]
