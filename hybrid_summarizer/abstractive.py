# This file contains the code for abstractive summarization using Pegasus and BART
from transformers import PegasusForConditionalGeneration, BartForConditionalGeneration, PegasusTokenizer, BartTokenizer

class AbstractiveSummarizer:
    def __init__(self, model_type):
        if model_type == 'pegasus':
            self.tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-cnn_dailymail')
            self.model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-cnn_dailymail')
        elif model_type == 'bart':
            self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
            self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    
    def summarize(self, text):
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
