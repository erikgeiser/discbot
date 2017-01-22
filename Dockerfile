from debian:stretch

RUN apt-get update
RUN apt-get install -y \
  python3 \
  python3-dev \
  python3-pip \
  libopus0 \
  libffi-dev
RUN apt-get clean
RUN pip3 install \
  aiohttp \
  websockets \
  PyNacl \
  discord.py[voice]

RUN ["bash"]
