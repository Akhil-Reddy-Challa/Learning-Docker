# Docker Container

This container is bundled with alpine and python, which operates on a given directory's text files.

Steps to Run:

1. Pull the container from docker hub

   > docker push akhil9/cloud-assignment:latest

2. Running the container
  
   On Linux Machine:

   > docker run -v $(pwd)/your/system/dir/with/text/files:/home/data akhil9/cloud-assignment

   On Windows Powershell:

   > docker run -v ${PWD}/your/system/dir/with/text/files:/home/data akhil9/cloud-assignment

   On Windows Commandline:

   > docker run -v %cd%/your/system/dir/with/text/files:/home/data akhil9/cloud-assignment
