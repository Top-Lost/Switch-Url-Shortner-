FROM python:latest
COPY . .
RUN pip3 install -r requirements.txt

CMD ["bash", "start.sh"]