FROM python:3.11
WORKDIR /service
COPY requirements_dev.txt .
COPY . ./
RUN pip install -r requirements_dev.txt
#ENTRYPOINT [ "streamlit","app.py" ]
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]