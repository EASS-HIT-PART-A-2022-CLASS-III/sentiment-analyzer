#~~~~~~~~~~~~~~~~~ IMPORTS ~~~~~~~~~~~~~~~~~~~~
import streamlit as st
import requests

#~~~~~~~~~~~~~~~~~ ENDPOINTS ~~~~~~~~~~~~~~~~~~~~
#backend_url = "http://0.0.0.0:8000"
backend_url = "http://backend:8000"
options = ["sentiment", "summarize", "keywords"]

#~~~~~~~~~~~~~~~~~ PAGE CONFIGURATION ~~~~~~~~~~~~~~~~~~~~

st.set_page_config(
    page_title="Sentiment Analyzer App",
    page_icon="🦾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#~~~~~~~~~~~~~~~~~ REQUESTS BUILDER ~~~~~~~~~~~~~~~~~~~~
def make_request(option, text):
    url = f"{backend_url}/{option}"
    payload = {"text": f"{text}"}
    response = requests.post(url, json=payload)
    return response.json()

#~~~~~~~~~~~~~~~~~ STREAMLIT UI PAGE ~~~~~~~~~~~~~~~~~~~~
def main():
    st.markdown("<h1 style='color: Teal;'>Sentiment Analyzer 💡</h1>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='color: Silver;'>🔬 Smart app that allows you to analyze text. 📄</h3>",
                unsafe_allow_html=True)
    st.markdown("<span style='color: DarkCyan;'>Select the way you want tp analyze your text :</span>",
                unsafe_allow_html=True)
    st.markdown("<span style='color: DarkCyan;'>1. sentiment --> Enter a text and get the sentiment (positive/neutral/negative)</span>",
                unsafe_allow_html=True)
    st.markdown("<span style='color: DarkCyan;'>2. summarize --> Enter a long sentence to summarize it (in this method please wait up to 30seconds)</span>",
                unsafe_allow_html=True)
    st.markdown("<span style='color: DarkCyan;'>3. keywords --> Enter a text to extract the keywords in it \n</span>",
                unsafe_allow_html=True)



    selected_option = st.selectbox("Select an option", options)

    text_input = st.text_area("Enter the text")

    if st.button("Process"):
        if text_input:
            # Make the request to the backend API
            response = make_request(selected_option, text_input)

            st.subheader("Results :")
            st.json(response)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()

# ~~~~~~~~~~~~~~~~~ Run the Proj - for testing ~~~~~~~~~~~~~~~~~~~~

#docker build -t my_front .
#docker run -p 8501:8501 -it my_front

# to run only streamlit (test porpuse) :

#streamlit run gui.py