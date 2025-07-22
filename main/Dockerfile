FROM python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
ENV FLASK_APP=main.py
# Changing file mode as executing script

RUN chmod +x /app/migrate.sh
ENTRYPOINT ["/app/migrate.sh"]
CMD ["/app/migrate.sh"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]