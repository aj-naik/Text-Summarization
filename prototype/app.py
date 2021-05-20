from os import truncate
import streamlit as st 
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

def main():
    st.title("Text Summarization")
    st.markdown("AI web app to summarize text")

    text = st.text_area('Enter Text to Summarise', height=275)
    
    tokenizer = AutoTokenizer.from_pretrained('t5-base')
    model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict = True)

    if st.button("Summarize"):
        inputs = tokenizer.encode("Summarize:" + text, return_tensors = 'pt', truncation = True)

        summary_ids = model.generate(inputs, min_length=20, length_penalty=5., num_beams=2)

        summary = tokenizer.decode(summary_ids[0])

        res = st.write(summary)

if __name__ == '__main__':
    main()