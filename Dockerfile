FROM alpine

WORKDIR /

COPY *.py .

RUN apk add --update python3

RUN apk add --update py-pip

RUN pip install prettytable

CMD ["python3", "WordCounter.py"]

# 1) Building Docker Image
    # docker build -t akhil9/cloud-assignment .

# 2) Running/testing this specific docker image
    # On Linux: 
    # docker run -v "$(pwd)"/target:/home/data akhil9/cloud-assignment

    # On Windows command prompt: 
    # docker run -v %cd%:/home/data akhil9/cloud-assignment

    # On Windows powershell: 
    # docker run -v ${PWD}:/home/data akhil9/cloud-assignment

# 3) Pushing Image to Docker repo
    # docker push akhil9/cloud-assignment:latest

#########################################################################

# Saving docker image without using pull command

# 1) Get Docker Image
    # docker save akhil9/cloud-assignment > M13958007_cloud-assignment.tar

# 2) Load the Image
    # docker load -i M13958007_cloud-assignment.tar

# 3) Run the Image
    # docker run -v "$(pwd)"/target:/home/data akhil9/cloud-assignment
