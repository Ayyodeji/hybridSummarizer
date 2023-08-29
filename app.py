from flask import Flask, render_template, request
from hybrid_summarizer.extractive import ExtractiveSummarizer
from hybrid_summarizer.abstractive import AbstractiveSummarizer
from hybrid_summarizer.utils import cosine_similarity_pruning

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    
    if request.method == 'POST':
        input_text = request.form['input_text']
        
        # Extractive summarization using BERT
        extractive_summarizer = ExtractiveSummarizer()
        extractive_summary = extractive_summarizer.summarize(input_text)
        
        # Abstractive summarization using Pegasus and BART
        pegasus_summarizer = AbstractiveSummarizer('pegasus')
        bart_summarizer = AbstractiveSummarizer('bart')
        pegasus_summary = pegasus_summarizer.summarize(input_text)
        bart_summary = bart_summarizer.summarize(input_text)
        
        # Combine and prune using cosine similarity
        all_summaries = [extractive_summary, pegasus_summary, bart_summary]
        pruned_summary = cosine_similarity_pruning(extractive_summary, all_summaries)
        
        summary = " ".join(pruned_summary)
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
