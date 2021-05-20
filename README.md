# Text-Summarization
Text summarization using Transformers. 

# Project History
I wanted to create an abstractive text summarization app as a tool to help in university studies. Researched and tried various models for text summarization including LSTMS and RNNs etc. The output was okay enough from a project point of view but not good enough for actual use case. Transformers produce good enough summary for real world use case. According to my tests with both T5 and Pegasus, Pegasus produced slightly better output than T5.

# Project
1. 'src' directory contains notebooks for t5 and pegasus models.
2. 'prototype' directory contains a web app prototype created using Streamlit framework for testing purposes. To run it locally:-
    1. Git Clone repo
    2. Go to 'prototype' directory, open command prompt there and run 'streamlit run app.py'

# Tech Used 
These are the libraries and technologies used or will be used in the project.
1. PyTorch 
2. Transformers Library
3. Streamlit
4. Flask (Work in Progress)

# To Do
1. Create a web app using Flask and host on cloud platforms for easy usage.
2. Build a chrome extension for use in web site (More portable and faster than web app).
