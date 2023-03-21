FROM ubuntu:18.04
USER 0

WORKDIR /app

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/results
RUN mkdir -p /app/mount-folder
RUN chmod -R 777 /app

ENTRYPOINT /bin/bash -c "source /app/entryw.sh"
