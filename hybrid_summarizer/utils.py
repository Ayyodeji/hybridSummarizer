# This file contains utility functions
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def cosine_similarity_pruning(sentences, summary_candidates, threshold=0.8):
    # Calculate cosine similarities between sentences and summary candidates
    sentence_embeddings = np.array([np.mean(model.encode(sentence.split()), axis=0) for sentence in sentences])
    summary_embeddings = np.array([np.mean(model.encode(candidate.split()), axis=0) for candidate in summary_candidates])
    similarities = cosine_similarity(sentence_embeddings, summary_embeddings)
    
    # Prune sentences that are too similar to summary candidates
    selected_indices = []
    for i in range(similarities.shape[0]):
        if all(similarities[i] < threshold):
            selected_indices.append(i)
    return [sentences[i] for i in selected_indices]
