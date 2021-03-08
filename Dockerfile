FROM alpine

WORKDIR /

COPY *.py .

RUN apk add --update python3

CMD ["python3", "WordCounter.py"]

# 1) Build Docker Image
# docker build -t akhil9/cloud-assignment .

# 2) Run/test the docker image 
# docker run -v "$(pwd)"/target:/home/data akhil9/cloud-assignment

# 3) Push to Docker repo
# docker push akhil9/cloud-assignment:latest