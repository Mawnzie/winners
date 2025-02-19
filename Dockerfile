FROM python
WORKDIR /app
RUN pip install pandas
ENTRYPOINT ["python"]
