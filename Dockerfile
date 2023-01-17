ARG LEPRIKON_TAG=latest
FROM leprikon/leprikon:$LEPRIKON_TAG

LABEL maintainer="Jakub Dorňák <jakub.dornak@qbsoftware.cz>"

# install requirements
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy files
COPY domecekhorovice /app/domecekhorovice

ENV SITE_MODULE=domecekhorovice

# run this command at the end of any dockerfile based on this one
RUN leprikon collectstatic --no-input
