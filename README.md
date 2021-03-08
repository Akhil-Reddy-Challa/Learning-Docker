# Docker Container
This container is bundled with alpine and python, which operates on a given directory's text files.

Steps to Run:
1) Pull the container from docker hub
  > docker push akhil9/cloud-assignment:latest
2) Run the container
  > docker run -v your/system/dir/with/text/files:/home/data akhil9/cloud-assignment
