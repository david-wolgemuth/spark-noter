### README.md

# Book Metadata and Chapter Summarizer

This project is a Python tool that generates metadata and summaries for books by parsing HTML content. The tool leverages OpenAI's GPT-3.5-turbo-16k model for natural language processing, Jinja2 for templating, and BeautifulSoup for HTML parsing.

## Features

- Generate metadata for an entire book.
- Generate summaries for individual chapters.
- Extract and structure book content, including titles, summaries, events, reading difficulty, characters, and locations.
- Command-line interface for easy usage.

## Requirements

- Python 3.x
- OpenAI API
- BeautifulSoup
- Jinja2

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/book-metadata-summarizer.git
   cd book-metadata-summarizer
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the OpenAI API key in your environment:
   ```sh
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage

### Command-line Interface

The tool can be used via the command line to generate metadata and summaries for books and chapters.

### Generate Metadata and Summaries for a Book

To generate metadata and summaries for an entire book, use the following command:

```sh
python3 main.py -i path/to/book.html -o path/to/output.html
```

### Generate Summary for a Specific Chapter

To generate a summary for a specific chapter, use the `--chapter` option with the chapter number (1-indexed):

```sh
python3 main.py -i path/to/book.html -o path/to/output.html -c 1
```

### Examples

#### Example 1: Generating Book Metadata and Summaries

```sh
python3 main.py -i examples/alice_in_wonderland.html -o output/alice_in_wonderland_summary.html
```

#### Example 2: Generating Chapter Summary

```sh
python3 main.py -i examples/alice_in_wonderland.html -o output/chapter_1_summary.html -c 1
```

## Templates

The project uses Jinja2 templates for rendering prompts and summaries. Templates are stored in the `templates` directory:

- `chapter_summary_system.md`
- `chapter_summary_user.md`
- `book_metadata_system.md`
- `book_metadata_user.md`
- `chapter_summary.html`
- `book_summary.html`

## Example Output

The generated HTML output includes structured metadata and summaries, making it easy to read and understand the content of the book.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- OpenAI for their powerful language models.
- BeautifulSoup for HTML parsing.
- Jinja2 for templating.

## Contact

For any questions or feedback, please contact [your-email@example.com].

---

Happy summarizing!
