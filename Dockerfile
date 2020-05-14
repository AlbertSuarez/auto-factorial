# Create base image
FROM python:3.7
ADD . /srv/auto-factorial
WORKDIR /srv/auto-factorial

# Install Firefox
RUN wget https://ftp.mozilla.org/pub/firefox/releases/75.0/linux-x86_64/en-US/firefox-75.0.tar.bz2
RUN tar xvf firefox-75.0.tar.bz2
RUN mv firefox/ /usr/lib/firefox
RUN ln -s /usr/lib/firefox /usr/bin/firefox

# Install Python requirements
RUN pip install --upgrade pip
RUN pip3 install -r requirements.lock

# Run application
CMD python3 -m src
