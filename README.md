# Text-Summarization
Abstractive and Extractive Text summarization Transformer model and API. 

# Project History
I wanted to create an abstractive text summarization app as a tool to help in university studies. Researched and tried various models for text summarization including LSTMS and RNNs etc. The output was okay enough from a project point of view but not good enough for actual use case.
Hence I decided to go with Transformers which produce good enough summary for real world use case. I used T5, Pegasus Longformer2RoBerta, BART and LED . According to my tests the models surprisingly, Pegasus produced  better output than the other two. Longformer2RobBerta should have been the best model as it is meant to be used for summarization of long documents but the output produced wasn't upto the mark. BART and LED also gave decentish outputs. Overall Pegasus provided a good abstractive summary

Also tried a few extractive based transformer models like BERT, GPT2, XLNet. The output was almost indistingushible from a human summary.

# Project
1. 'src' directory contains 3 sub directories:
- 'abstractive' which contains notebooks for T5, Pegasus, Longformer2RoBerta, BART and LED abstractive summarization models.
- 'extractive' which contains BERT, GPT2 and XLNet extractive summarization models.
2. 'prototype' directory contains a web app prototype created using Streamlit framework (Used T5) for testing purposes. To run it locally:-
    - Git Clone repo
    - Go to 'prototype' directory, open command prompt there and run 'streamlit run app.py'
3. 'app' directory contains an API created for both Abstractive and Extractive (Pegasus and XLNet) summaries. To test API locally:
- Run <code>pip install -r requirements.txt</code> to install all dependencies
- Open terminal in project directory and run <code>uvicorn app.main:app --reload</code>
- After the application startup is completed, go to <code>localhost:8000/docs</code> to try it out

Note:- 
- API will soon be deployed to cloud for inference and then integrated into FLASK application as direct usage of transformer leads to timeout.
- Dont copy paste 2 paras directly while testing. Remove all instances of new line so as to convert text to 1 continuous paragraph. Otherwise it will lead to Error 422. 

# Tech Used 
These are the libraries and technologies used or will be used in the project.
1. PyTorch 
2. Transformers Library
3. Streamlit
4. Flask (Work in Progress)
5. FastAPI

# To Do
1. ~~Create a web app using Flask and host on cloud platforms for easy usage.~~ (Done)
2. Build a chrome extension for use in web site (More portable and faster than web app). (WIP)
