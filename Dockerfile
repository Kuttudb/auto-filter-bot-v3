# Python Based Docker
FROM python:latest

# Installing Packages
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y

# Updating Pip Packages
RUN pip3 install -U pip

# Copying Requirements
COPY requirements.txt /requirements.txt

# Installing Requirements
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /auto-filter-bot-v3
WORKDIR /auto-filter-bot-v3
COPY start.sh /start.sh

# Running auto-filter-bot-v3
CMD ["/bin/bash", "/start.sh"]
