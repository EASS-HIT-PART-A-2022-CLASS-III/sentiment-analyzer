FROM python:3.9
WORKDIR /frontend
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "gui.py", "--server.port=8501", "--server.address=0.0.0.0"]

