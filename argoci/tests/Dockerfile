FROM joyzoursky/python-chromedriver:3.9-alpine
RUN pip install selenium 
RUN pip install requests
WORKDIR /
COPY test2.py /tests 
CMD pytest test2.py
