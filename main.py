import argparse
import sys
from rich.console import Console
from rich.text import Text
from tiktoken import get_encoding, list_encoding_names

COLORS = [
    {   # Purple
        'text': '#6b40d8',
        'highlight': '#362a59'
    },
    {   # Green
        'text': '#68de7a',
        'highlight': '#3c6d46'
    },
    {   # Yellow
        'text': '#f4ac36',
        'highlight': '#75592a'
    },
    {   # Red
        'text': '#ef4146',
        'highlight': '#732e31'
    },
    {   # Blue
        'text': '#27b5ea',
        'highlight': '#225c73'
    }
]

def tokenize(text, encoding_name="gpt-4o"):
    tokenizer = get_encoding(encoding_name)
    tokens = [t.decode('utf-8', errors='replace') for t in tokenizer.decode_tokens_bytes(tokenizer.encode(text, allowed_special="all"))]
    return tokens


def colorize_tokens(tokens, mode='highlight'):
    text = Text()
    num_colors = len(COLORS)
    for i, token in enumerate(tokens):
        color_name = COLORS[i % num_colors]
        if mode == 'text':
            style = color_name['text']
        elif mode == 'highlight':
            style = f"white on {color_name['highlight']}"
        text.append(token, style=style)
    return text

def calculate_stats(text, tokens):
    return {
        "tokens": len(tokens),
        "characters": len(text)
    }

def main():
    parser = argparse.ArgumentParser(
        description="Visualize tokenized text."
    )
    parser.add_argument(
        'input_file', nargs='?', type=argparse.FileType('r'),
        default=sys.stdin,
        help="Path to the input text file. Reads from stdin if not provided."
    )
    parser.add_argument(
        '--tokenizer', type=str, default="o200k_base",
        help="Tokenizer to use for tokenization. Possible values: " + ", ".join(list_encoding_names()) + " (default: o200k_base)"
    )
    parser.add_argument(
        '--mode', choices=['text', 'highlight'], default='highlight',
        help="Mode for displaying tokens: 'text' or 'highlight'. (default: highlight)"
    )
    parser.add_argument(
        '--hide-text', action="store_true",
        help="Hide the tokenized text."
    )
    parser.add_argument(
        '--hide-stats', action="store_true",
        help="Hide the token and character counts at the end."
    )
    parser.add_argument(
        '--force-terminal', action="store_true", default=None,
        help="Force terminal output."
    )

    args = parser.parse_args()

    if args.hide_text and args.hide_stats:
        parser.error("Cannot hide both text and stats.")

    console = Console(force_terminal=args.force_terminal)

    input_text = ""
    try:
        input_text = args.input_file.read()

    finally:
        if args.input_file is not sys.stdin:
            args.input_file.close()

    tokens = tokenize(input_text, args.tokenizer)

    if not args.hide_text:
        rich_text = colorize_tokens(tokens, args.mode)
        console.print(rich_text)

    if not args.hide_stats:
        stats = calculate_stats(input_text, tokens)
        if not args.hide_text and input_text:
            console.print()
        console.print(f"{stats['tokens']} tokens, {stats['characters']} characters")

if __name__ == "__main__":
    main()
