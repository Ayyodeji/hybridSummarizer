# This is the main script to run the hybrid summarization

from hybrid_summarizer.extractive import ExtractiveSummarizer
from hybrid_summarizer.abstractive import AbstractiveSummarizer
from hybrid_summarizer.utils import cosine_similarity_pruning

def main():
    input_text = "input" #Enter your input here
    
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
    
    print("Extractive Summary:", extractive_summary)
    print("Pegasus Summary:", pegasus_summary)
    print("BART Summary:", bart_summary)
    print("Pruned Summary:", pruned_summary)

if __name__ == "__main__":
    main()
