FROM python:3.9
#working directory
WORKDIR /backend
COPY . .
#Python dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#to run build+run docker :

#docker build -t my_docker .
#docker run -p 8000:8000 -it my_docker

# to run only uvicorn and fastAPI (test porpuse) :

#uvicorn main:app --host 0.0.0.0 --port 8000