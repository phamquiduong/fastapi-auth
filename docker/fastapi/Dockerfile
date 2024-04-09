FROM python:3
ENV PYTHONUNBUFFERED 1


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip


# Install python packet
COPY requirements.txt /
RUN pip install -r requirements.txt
