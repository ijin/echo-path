FROM python:latest
COPY server.py .
EXPOSE 8000
CMD python server.py

