# Hybrid Summarizer

Hybrid Summarizer is a web application that combines extractive and abstractive summarization techniques to generate concise summaries of input text.
Hybrid Summarizer utilizes both extractive summarization (using BERT) and abstractive summarization (using Pegasus and BART) to create summaries that capture key information from input text. The summaries are then combined and pruned using cosine similarity to produce a refined summary.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Description

The Hybrid Summarizer model architecture represents a cohesive fusion of extractive and abstractive summarization methodologies, aiming to distill the core essence of input text into succinct and coherent summaries. It initiates the process with extractive summarization, employing the BERT architecture to comprehend the contextual significance of sentences through tokenization and embedding calculations. This results in the identification of salient sentences, forming the basis of the extractive summary. Transitioning seamlessly, the abstractive phase harnesses the prowess of both Pegasus and BART models, adept at generating summaries by predicting cohesive phrases that encapsulate the thematic core of the text. The culmination lies in the synthesis of these paradigms, wherein the generated extractive and abstractive summaries are strategically amalgamated. To ensure coherence, a cosine similarity-based pruning mechanism adeptly curates the final summary by eliminating redundant overlaps between the extractive and abstractive components. Thus, the Hybrid Summarizer model stands as a testament to the harmonious collaboration between disparate yet complementary techniques, ultimately resulting in summaries that encapsulate both factual relevance and linguistic eloquence

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Ayyodeji/hybridSummarizer.git
   ```



2. Navigate to the project directory:

   ```bash
   cd hybrid-summarizer
   ```

3. Install the required dependencies:

   ```bash
   pip install -e .
   ```

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000/`.
3. Enter the input text and click "Summarize" to see the generated summary.

## Project Structure

The project follows this directory structure:

```
hybrid_summarizer_project/
│
├── hybrid_summarizer/
│   ├── __init__.py
│   ├── extractive.py
│   ├── abstractive.py
│   ├── utils.py
│
├── templates/
│   ├── index.html
│
├── app.py
├── setup.py
```

- `hybrid_summarizer`: Contains modules for extractive and abstractive summarization.
- `templates`: Contains the HTML template for the Flask app.
- `app.py`: Main script to run the Flask app.
- `setup.py`: Project setup script.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bugfix: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Create a pull request.
