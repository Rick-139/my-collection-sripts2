def convert_markdown_to_html(markdown_text):
    """Convert Markdown text to HTML."""
    html_lines = []
    lines = markdown_text.splitlines()

    for line in lines:
        if line.startswith('# '):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith('## '):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith('### '):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith('- '):
            html_lines.append(f"<li>{line[2:]}</li>")
        elif line.startswith('**') and line.endswith('**'):
            html_lines.append(f"<strong>{line[2:-2]}</strong>")
        elif line.startswith('*') and line.endswith('*'):
            html_lines.append(f"<em>{line[1:-1]}</em>")
        else:
            html_lines.append(f"<p>{line}</p>")

    return '\n'.join(html_lines)

def main():
    markdown_text = """# Sample Markdown
This is a **bold** text and this is *italic* text.

## List of Items
- Item 1
- Item 2
- Item 3

### Subheading
This is a paragraph under a subheading.
"""

    html_output = convert_markdown_to_html(markdown_text)
    print("Converted HTML:")
    print(html_output)

if __name__ == "__main__":
    main()
