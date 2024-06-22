import textwrap
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '*')
    text = textwrap.dedent(text).strip()

    return Markdown(text)
