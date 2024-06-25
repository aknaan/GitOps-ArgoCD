FROM python:3.12-slim
WORKDIR /project
COPY /project /project
RUN pip install -r requirements.txt && pip install pylint
CMD pylint ./* > codeanalysis/static_analysis.log

