import re

from pygments.lexer import RegexLexer, bygroups, combined, default, inherit
from pygments.lexers import SqlLexer
from pygments.token import Keyword, Name, Punctuation, Text, Whitespace


class BaldrSqlLexer(SqlLexer):
    name = "SQL for Baldr project"

    aliases = ["baldr-sql"]

    flags = re.DOTALL

    # def get_tables(lexer, match):
    #     print(match)
    #     table = match.group(0).split(',')
    #     print(table)
    #     for t in table:
    #         table_match = re.match(r'\s*(\w+)(\s+AS\s+(\w+)\s*)?', t)
    #         yield 0, Name.Class, table_match.group(1)
    #         print(table_match)
    #         if table_match.group(3):
    #                 yield 323, Name.Class, table_match.group(3)

    tokens = {
        "root": [
            (r"(FROM)(\s+)", bygroups(Keyword, Whitespace), "table-name-simple"),
            (r"[a-z_][\w]*(?=\.[a-z_][\w]*)", Name.Class),
            (r"(?<=\w\.)[a-z_][\w]*", Name.Attribute),
            (
                r"(\w+)(\s+)(AS)(\s+)(\w+)",
                bygroups(Name.Class, Whitespace, Keyword, Whitespace, Name.Class),
            ),
            # (r'(?<=FROM).*?(?=(WHERE|ORDER BY|$))', get_tables),
            inherit,
        ],
        # 'tablelist': [
        #     (r'(\w)( AS (\w))?,?', bygroups(Name.Class, Text, Name.Class))
        # ]
        "table-name-as": [
            (r"\s+", Whitespace),
            (
                r"(\w+)(\s+)(AS)(\s+)(\w+)",
                bygroups(Name.Class, Whitespace, Keyword, Whitespace, Name.Class),
            ),
            (r",", Punctuation, combined("table-name-as", "table-name-simple")),
            (r"", Text, "#pop"),
            default("root"),
        ],
        "table-name-simple": [
            (
                r"(\w+)(\s*)",
                bygroups(Name.Class, Whitespace),
            ),
            (r"(,)(\s*)", bygroups(Punctuation, Whitespace), "table-name-simple"),
            (r"", Text, "#pop"),
            # default("root")
        ],
    }

    def get_tokens_unprocessed(self, text: str):
        for item in RegexLexer.get_tokens_unprocessed(self, text):
            # print(item)
            yield item
