#~~~~~~~~~~~~~~~~~ IMPORTS ~~~~~~~~~~~~~~~~~~~~
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from transformers import pipeline
import numpy as np
import re
import nltk
from rake_nltk import Rake
import json

#~~~~~~~~~~~~~~~~~ ML models downloads ~~~~~~~~~~~~~~~~~~~~

nltk.download('stopwords')
nltk.download('punkt')

#~~~~~~~~~~~~~~~~~ FastAPI backend ~~~~~~~~~~~~~~~~~~~~

app = FastAPI()

#~~~~~~~~~~~~~~~~~ pydanric classes ~~~~~~~~~~~~~~~~~~~~

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    polarity: float

class TextSummarizationRequest(BaseModel):
    text: str

class TextSummarizationResponse(BaseModel):
    summary: str

class KeywordExtractionRequest(BaseModel):
    text: str

class KeywordExtractionResponse(BaseModel):
    keywords: list

#~~~~~~~~~~~~~~~~~ external funcs ~~~~~~~~~~~~~~~~~~~~

def keep_words_only(sentence):
    # Use regular expression pattern to match words
    pattern = r'\b\w+\b'
    # Find all matches in the sentence
    words = re.findall(pattern, sentence)
    # Join the matched words into a sentence
    result = ' '.join(words)
    return result


#~~~~~~~~~~~~~~~~~ FastAPI methods ~~~~~~~~~~~~~~~~~~~~
@app.get("/")
def land_page():
    return {"message" : "Welcome to Sentiment : your santiment analyzer API"}

# This method will analyze the sentiment of a sentence to negative/neutral/possitive.
@app.post("/sentiment")
def sentiment(request: SentimentRequest):
    blob = TextBlob(request.text)
    polarity = np.round(blob.sentiment.polarity, 2)
    sentiment = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    return SentimentResponse(sentiment=sentiment, polarity=polarity)

# This method will summarize huge sentence into a smaller one
@app.post("/summarize")
def summarize(request: TextSummarizationRequest):
    # Load text summarization pipeline from Hugging Face Transformers
    summarization_pipeline = pipeline("summarization")
    # Get text summary
    new_text = keep_words_only(request.text)
    result = summarization_pipeline(new_text, max_length=100, min_length=30, do_sample=True)
    summary = result[0]['summary_text'].strip()
    return TextSummarizationResponse(summary=summary)

#This method will extract the keywords from a huge sentece
@app.post("/keywords")
def extract_keywords(request: KeywordExtractionRequest):
    rake = Rake()
    # Extract keywords from text
    rake.extract_keywords_from_text(request.text)
    keywords = rake.get_ranked_phrases()
    return KeywordExtractionResponse(keywords=keywords)

#~~~~~~~~~~~~~~~~~ Run the Proj - for testing ~~~~~~~~~~~~~~~~~~~~

#to run build + run docker :
#docker build -t my_docker .
#docker run -p 8000:8000 -it my_docker

# to run only uvicorn and fastAPI (test porpuse) :
#uvicorn main:app --host 0.0.0.0 --port 8000