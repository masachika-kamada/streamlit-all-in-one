FROM mcr.microsoft.com/devcontainers/python:3.10

RUN apt-get update && \
    apt-get install -y \
        poppler-utils \
        ffmpeg

EXPOSE 8501

ENV TZ Asia/Tokyo 