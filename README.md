````markdown
# Hybrid Summarizer

Hybrid Summarizer is a web application that combines extractive and abstractive summarization techniques to generate concise summaries of input text.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Description

Hybrid Summarizer utilizes both extractive summarization (using BERT) and abstractive summarization (using Pegasus and BART) to create summaries that capture key information from input text. The summaries are then combined and pruned using cosine similarity to produce a refined summary.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/hybrid-summarizer.git
   ```
````

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

## License

This project is licensed under the [MIT License](LICENSE).

```

Replace `"your-username"` in the repository URL with your actual GitHub username, and feel free to customize any other information as needed. This `README.md` provides a basic structure for introducing your project, explaining its usage, showcasing the project structure, inviting contributions, and mentioning the license.
```
