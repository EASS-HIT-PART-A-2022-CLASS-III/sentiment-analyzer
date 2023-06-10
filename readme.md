*** 

# Sentiment Analyzer 🦾️

🔬 Smart app that allows you to analyze text. 📄

This document will provide you with a brief overview of the application and its functionalities,
as well as instructions for installation and usage.

- DEMO Video : https://youtu.be/IEYMgwdf7-U
<iframe width="560" height="315" src="https://www.youtube.com/embed/IEYMgwdf7-U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
***

## Getting Started
***
### Overviwe: 

The apps porpuse is to analyze your text by analyzing its sentiment , key words and summarizeation tool . 

This app is desinged in microservices type of architecture. 

*  Backend : 'fastAPI' + 'Pydantic' + ML Models (Dockerized)
* QA and Testing : 

-Tests : 'unittest' and 'fastapi.testclient'

-Logs : 'logging' 
*  Frontend : 'streamlit' + 'requests' (Dockerized)


![img_1.png](img_1.png)


***


### Installation

First, clone the repo : 
```
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-III/sentiment-analyzer.git
```
Navigate to main folder and run :

```
docker-compose up
```
To run backend , navigate to backend folder and run :

```
docker build -t my_docker .
docker run -p 8000:8000 -it my_docker
```
To run frontend , navigate to frontend folder and run :
```
#docker build -t my_front .
#docker run -p 8501:8501 -it my_front
```
***
## Help
Any advise for common problems or issues.
```
yossidv@hotmail.com
```
