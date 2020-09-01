
import streamlit as st
#packages
import spacy
from textblob import TextBlob
def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
   
    tokens = [token.text for token in docx]
    return tokens

def main():
    st.title("NLPify")
    st.subheader("cligi")


    if st.checkbox("show tokens"):
        st.subheader("tokenize your text")
        message = st.text_area("enter ur text", "type here")
        if st.button("Analyze"):
          nlp_result = text_analyzer(message)
          st.success(nlp_result)


if __name__ == '__main__':
    main()
