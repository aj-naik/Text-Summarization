from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from api.summary import Summary
import uvicorn

class Message(BaseModel):
    input: str
    output: str = None

app = FastAPI()
summary = Summary()

@app.get('/')
def get_root():
	return {'message': 'Welcome to the text summarization API'}

@app.post("/abs-summary/")
async def  abssummary(message: Message):
    message.output  = summary.abs_summary(text=message.input)
    return {"output" : message.output}

@app.post("/ext-summary/")
async def extsummary(message: Message):
    message.output  = str(summary.ext_summary(message.input))
    return {"output" : message.output}


    