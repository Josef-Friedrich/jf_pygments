from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Whitespace,
)


class WhiteStyle(Style):
    """All fonts are changed to white."""

    background_color = "#ffffff"

    styles = {
        Comment: "#ffffff",
        Keyword: "#ffffff",
        Operator: "#ffffff",
        Name: "#ffffff",
        String: "#ffffff",
        Generic: "#ffffff",
        Error: "#ffffff",
        Literal: "#ffffff",
        Number: "#ffffff",
        Whitespace: "#ffffff",
        Punctuation: "#ffffff",
    }
