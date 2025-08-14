FROM registry.access.redhat.com/ubi9/python-311
WORKDIR /opt/app-root/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY gunicorn.conf.py .
ENV PORT=8080
EXPOSE 8080
CMD ["gunicorn", "app.main:app"]