import os
os.environ['FLASK_ENV'] = 'production'

import streamlit as st
from pickle import load

vector = load(open("vector_tfidf.sav", "rb"))
model = load(open("bernoulli_spam.sav", "rb"))

def predict_spam(str):
    sentence = [str.strip().lower().replace('\t', ' ').replace('\n', ' ').replace('.', '')]
    sentence_vector = vector.transform(sentence).toarray()
    prediction = model.predict(sentence_vector)
    if prediction == 1:
        return 'Spam'
    else:
        return 'Not spam'

def main():
    st.title("SMS Spam Analysis")
    review = st.text_input("Enter the SMS:")

    if st.button("Submit"):
        result = predict_spam(review)
        st.write(f"Classification: {result}")

#if __name__ == "__main__":
#   main()


