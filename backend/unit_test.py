import unittest
import logging
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest import TestCase
from main import app, SentimentRequest, TextSummarizationRequest, KeywordExtractionRequest

class TestApp(TestCase):

    def setUp(self):
        self.client = TestClient(app)
        logging.basicConfig(filename="log_test.txt", level=logging.INFO)

    def log_result(self, result):
        if result.wasSuccessful():
            logging.info("Test case: %s - PASSED", result)
        else:
            logging.error("Test case: %s - FAILED", result)

    def test_land_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.log_result(self._outcome.result)

    def test_sentiment(self):
        request = SentimentRequest(text="I am happy")
        response = self.client.post("/sentiment", json=request.dict())
        self.assertEqual(response.status_code, 200)
        self.log_result(self._outcome.result)

    def test_summarize(self):
        request = TextSummarizationRequest(text="This is a long text that needs to be summarized.")
        response = self.client.post("/summarize", json=request.dict())
        self.assertEqual(response.status_code, 200)
        self.log_result(self._outcome.result)

    def test_extract_keywords(self):
        request = KeywordExtractionRequest(text="This is a long text from which we need to extract keywords.")
        response = self.client.post("/keywords", json=request.dict())
        self.assertEqual(response.status_code, 200)
        self.log_result(self._outcome.result)
