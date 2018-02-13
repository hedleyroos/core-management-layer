FROM praekeltfoundation/python-base:3.6-stretch

WORKDIR /app

COPY requirements.txt /app/requirements/

RUN pip3 install --no-cache-dir -r /app/requirements/requirements.txt

COPY . /app/

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["swagger_server/httpd.py", "--logging=debug"]
