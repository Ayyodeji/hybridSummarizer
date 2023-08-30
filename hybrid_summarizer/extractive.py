# This file contains the code for extractive summarization using BERT
import torch
from transformers import BertTokenizer, BertModel
import numpy as np

class ExtractiveSummarizer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
    
    def summarize(self, text, num_sentences=3):
        # Tokenize and encode the text
        inputs = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            sentence_embeddings = outputs.last_hidden_state.mean(dim=1)  # Average pooling
        
        # Calculate sentence importance scores
        sentence_scores = np.linalg.norm(sentence_embeddings, axis=1)
        top_indices = sentence_scores.argsort()[-num_sentences:][::-1]
        
        # Extract and return the top sentences
        sentences = text.split('.')
        summary = '. '.join([sentences[i] for i in top_indices])
        return summary
