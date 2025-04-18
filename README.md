<h1 align="center">Token CLI</h1>

<p align="center">A command-line tool to visualize tokenized text.</p>

![Demo](demo.gif)

## Usage

Clone this repo.

**From standard input:**

```bash
echo "This is sample text." | uv run main.py --stats
```

**From a file:**

```bash
uv run main.py --stats your_text_file.txt
```

**Usage with `fzf`**
```bash
fzf --preview "uv run main.py --stats --force-terminal {}"
```

## Options

```
usage: main.py [-h] [--mode {text,highlight}] [--hide-text] [--stats]
               [--force-terminal]
               [input_file]

Visualize tokenized text.

positional arguments:
  input_file            Path to the input text file. Reads from stdin if not
                        provided.

options:
  -h, --help            show this help message and exit
  --mode {text,highlight}
                        Mode for displaying tokens: 'text' or 'highlight'.
                        (default: highlight)
  --hide-text           Hide the tokenized text.
  --stats               Display token and character counts at the end.
  --force-terminal      Force terminal output.

```