FROM praekeltfoundation/python-base:3.6-stretch

WORKDIR /app

COPY requirements.txt /app/requirements/

# Git is required because one of the pip requirements is pulled from github.
RUN apt-get update
RUN apt-get install -y git

RUN pip3 install --no-cache-dir -r /app/requirements/requirements.txt

COPY . /app/

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["swagger_server/httpd.py", "--logging=debug"]
