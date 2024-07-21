FROM python:3.11
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements_dev.txt
ENTRYPOINT [ "python3","app.py" ]