import streamlit as st
import regex as re
from pickle import load
from nltk import download
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

download("wordnet")
lemmatizer = WordNetLemmatizer()
download("stopwords")
stop_words = stopwords.words("english")

st.title("SMS Spam Analysis")

def preprocess_text(text):
    # Remove any character that is not a letter (a-z) or white space ( )
    text = re.sub(r'[^a-z ]', " ", text)
    # Remove white spaces
    text = re.sub(r'\s+[a-zA-Z]\s+', " ", text)
    text = re.sub(r'\^[a-zA-Z]\s+', " ", text)
    # Multiple white spaces into one
    text = re.sub(r'\s+', " ", text.lower())
    # Remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)
    return text.split()

def lemmatize_text(words, lemmatizer = lemmatizer):
    tokens = [lemmatizer.lemmatize(word) for word in words]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if len(word) > 3]
    return tokens

def predict_spam(str):
    sentence = lemmatize_text(preprocess_text(str))
    tokens = [" ".join(tokens) for tokens in sentence]
    tokens_vector = vector.transform(tokens).toarray()
    prediction = model.predict(tokens_vector)
    if prediction.any() == 0:
        return 'Not spam'
    else:
        return 'Spam'
        
def my_streamlit_app():
    vector = load(open("vector_tfidf.sav", "rb"))
    model = load(open("xg_spam.sav", "rb"))
    
    review = st.text_input("Enter the SMS:")
    
    if st.button("Submit"):
        result = predict_spam(review)
        st.write(f"Classification: {result}")

if __name__ == '__main__':
    my_streamlit_app()


