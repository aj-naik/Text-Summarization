# Text-Summarization
Text summarization using Transformers. 

# Project History
I wanted to create an abstractive text summarization app as a tool to help in university studies. Researched and tried various models for text summarization including LSTMS and RNNs etc. The output was okay enough from a project point of view but not good enough for actual use case. So I decided to go with Transformers which produce good enough summary for real world use case.I used T5, Pegasus and Longformer2RoBerta. According to my tests the models surprisingly, Pegasus produced  better output than the other two. Longformer2RobBerta should have been the best model as it is meant to be used for summarization of long documents but the output produced wasn't upto the mark.

# Project
1. 'src' directory contains notebooks for T5, Pegasus and Longformer2RoBerta models.
2. 'prototype' directory contains a web app prototype created using Streamlit framework (Used T5) for testing purposes. To run it locally:-
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
