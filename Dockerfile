FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /book_wishlist
WORKDIR /book_wishlist

COPY requirements.txt /book_wishlist/
RUN pip install -r requirements.txt

COPY . /book_wishlist/