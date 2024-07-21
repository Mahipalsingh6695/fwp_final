FROM python:3.11
WORKDIR /service
COPY requirements.txt .
COPY . ./
RUN pip install -r requirements_dev.txt
ENTRYPOINT [ "python3","app.py" ]
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]