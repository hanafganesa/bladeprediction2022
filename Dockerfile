FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip sudo

RUN useradd -m hanaganesaf

RUN chown -R hanaganesaf:hanaganesaf /home/hanaganesaf/

COPY --chown=hanaganesaf . /home/hanaganesaf/app/

USER hanaganesaf

RUN pip3 install --upgrade pip

RUN cd /home/hanaganesaf/app/ && pip3 install -r requirements.txt

WORKDIR /home/hanaganesaf/app

EXPOSE 8080

ENTRYPOINT python3 app.py