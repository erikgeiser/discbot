# Discbot
Discbot is a folder based discord music bot.

## Build the image
This repository provides a Dockerfile to deploy the bot.

The Docker image can be built like this:
```
docker build -t discbot .
```

## Configurate the bot

Edit the file `config/config_sample.ini` and save it as `config/config.ini` to configurte the bot

## Run the bot

The docker image can be run like this:
```
docker run --rm -it -v ./discbot:/discbot -v ./config:/discbot/config discbot
cd /discbot
python3 run.py
```
