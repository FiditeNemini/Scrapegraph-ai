"""
convert_to_md modul
"""
import html2text

def convert_to_md(html):
    """ Convert HTML to Markdown.
    This function uses the html2text library to convert the provided HTML content to Markdown 
    format.
    The function returns the converted Markdown content as a string.

    Args: html (str): The HTML content to be converted.

    Returns: str: The equivalent Markdown content.

    Example: >>> convert_to_md("<html><body><p>This is a paragraph.</p>
    <h1>This is a heading.</h1></body></html>") 
    'This is a paragraph.\n\n# This is a heading.'

    Note: All the styles and links are ignored during the conversion. """
    h = html2text.HTML2Text()
    h.ignore_links = False
    return h.handle(html)
