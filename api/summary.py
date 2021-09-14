
from transformers import  PegasusForConditionalGeneration, PegasusTokenizer
from transformers import pipeline
import re

class Summary:
    def __init__(self):
        self.sum_model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-large')
        self.sum_tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-large') 
         
    def abs_summary(self, text):
        
        text = text.strip('\n')
        text = text.strip('\t')
        batch = self.sum_tokenizer(text, truncation=True, padding='longest', return_tensors="pt")
        translated = self.sum_model.generate(**batch)
        tgt_text = self.sum_tokenizer.batch_decode(translated, skip_special_tokens=True)
        abs_result = tgt_text[0]
        return abs_result

    def ext_summary(self, text: str):

        text = text.replace('\n','')
        text = text.replace('\t','')
        summarizer = pipeline("summarization")
        summarized = summarizer(text, min_length=60)
        summary = summarized[0]
        ext_result = re.findall(r'"([^"]*)"', str(summary))
        return ext_result