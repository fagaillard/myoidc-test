FROM python:2

RUN pip install --no-cache-dir tornado netifaces

RUN mkdir /usr/app
# allow to run as non root
RUN chgrp -R 0 /usr/app && chmod -R g+rwX /usr/app
COPY index.py /usr/app/index.py
    
EXPOSE 8888

ENTRYPOINT ["python", "/usr/app/index.py"]
