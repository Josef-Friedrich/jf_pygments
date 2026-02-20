import re

from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import Keyword, Name, Punctuation, Whitespace


class TableSchemaLexer(RegexLexer):
    name = "Tabellenschema"

    aliases = ["table-schema"]

    flags = re.DOTALL

    tokens = {
        "root": [
            (
                r"(\w+)(\s*)(\()(\s*)",
                bygroups(Name.Class, Whitespace, Punctuation, Whitespace),
                "table",
            ),
        ],
        "table": [
            (
                r"(\w+)(:)(\s*)?",
                bygroups(Name.Attribute, Punctuation, Whitespace),
                "attribute",
            ),
            (r"\)", Punctuation, "#pop"),
        ],
        "attribute": [
            (
                r"(\w+)(:)(\s*)?",
                bygroups(Name.Attribute, Punctuation, Whitespace),
                "attribute",
            ),
            include("datatypes"),
            (r"(;)(\s*)?", bygroups(Punctuation, Whitespace), "attribute"),
            (r"\s*\)", Punctuation, "table"),
        ],
        "datatypes": [
            (
                words(
                    (
                        "Ganzzahl",
                        "Zahl",
                        "Wahrheitswert",
                        "Text",
                        "Datum",
                        "Gleitkommazahl",
                    ),
                    suffix=r"\b",
                ),
                Keyword.Type,
            ),
        ],
    }
