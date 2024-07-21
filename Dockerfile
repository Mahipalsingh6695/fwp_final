FROM python:3.11
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements_dev.txt
#ENTRYPOINT [ "streamlit","app.py" ]
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]