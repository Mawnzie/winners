FROM python
WORKDIR /app
RUN pip install pandas
#COPY ["winners.py", "Test.py" .
ENTRYPOINT ["python"]
