from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name


def debug(code: str, lexer: str):
    print(
        highlight(
            code,
            get_lexer_by_name(lexer),
            get_formatter_by_name("tokens"),
        ).decode("utf-8")
    )
    print(
        highlight(
            code,
            get_lexer_by_name(lexer),
            get_formatter_by_name("terminal256"),
        )
    )


debug("SELECT * FROM Person AS p WHERE lol = 3", "baldr-sql")

debug("SELECT * FROM Person , Lol WHERE lol = 3", "baldr-sql")
