FROM python:3.9
#working directory
WORKDIR /frontend
COPY . .
#Python dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
# Start FastAPI
CMD ["streamlit", "run", "gui.py"]

#docker build -t my_front .
#docker run -p 8501:8501 -it my_front

# to run only streamlit (test porpuse) :

#streamlit run gui.py