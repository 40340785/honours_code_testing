FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip iputils-ping
RUN pip3 install flask requests python-dateutil 
RUN mkdir /app && cd /app
CMD python3 /app/script.py
