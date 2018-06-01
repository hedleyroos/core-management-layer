FROM praekeltfoundation/python-base:3.6-stretch

WORKDIR /app

COPY requirements.txt /app/requirements/

# Git is required because one of the pip requirements is pulled from github.
RUN apt-get update && apt-get install -y git

RUN pip3 install --no-cache-dir -r /app/requirements/requirements.txt --src /usr/local/src

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["httpd.py", "--logging=DEBUG"]
