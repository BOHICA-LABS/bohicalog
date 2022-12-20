"""
Utility functions for telegram handler
"""


def escape_html(text):
    """
    Escapes all html characters in text

    :param str text: Text to escape
    :rtype: str
    :return: Escaped text
    """
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
