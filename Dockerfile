FROM tensorflow/tensorflow:2.4.0

RUN apt-get update -y

COPY ./docker_requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app/ app/

ENTRYPOINT [ "python" ]

CMD [ "app/app.py" ]
