FROM python
WORKDIR /app
RUN pip install pandas Flask
ENTRYPOINT ["python"]
