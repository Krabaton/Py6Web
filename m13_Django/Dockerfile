FROM python:3.10
RUN apt update
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
RUN chmod +x run.sh
CMD ["./run.sh"]
