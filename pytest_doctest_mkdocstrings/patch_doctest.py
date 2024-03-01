# noqa: D100
import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """Adds a commandline flag to enable handling markdown codeblocks in doctests."""

    collectiongroup = parser.getgroup("doctest", description="Doctest parsing")
    collectiongroup.addoption(
        "--doctest-mdcodeblocks",
        action = "store_true",
        help = "Allow markdown codeblocks enclosed with triple-ticks (```) in doctests.",
    )

def pytest_sessionstart(session: pytest.Session) -> None:
    """
    Monkeypatches DocTests Regex to ignore end of codeblock marker.

    Run by pytest before beginning collection
    """
    del session  # We don't need the session info

    import doctest
    import re

    # https://github.com/python/cpython/blob/a0a8d9ffe0ddb0f55aeb02801f48e722c2660ed3/Lib/doctest.py#L613

    _ORIGINAL_EXAMPLE_RE = re.compile(  # noqa: N806
        r"""
        # Source consists of a PS1 line followed by zero or more PS2 lines.
        (?P<source>
            (?:^(?P<indent> [ ]*) >>>    .*)    # PS1 line
            (?:\n           [ ]*  \.\.\. .*)*)  # PS2 lines
        \n?
        # Want consists of any non-blank lines that do not start with PS1.
        (?P<want> (?:(?![ ]*$)    # Not a blank line
                     (?![ ]*>>>)  # Not a line starting with PS1
                     .+$\n?       # But any other line
                  )*)
        """,
        re.MULTILINE | re.VERBOSE,
    )

    _MD_EXAMPLE_RE = re.compile(  # noqa: N806
        r"""
            # Source consists of a PS1 line followed by zero or more PS2 lines.
            (?P<source>
                (?:^(?P<indent> [ ]*) >>>    .*)    # PS1 line
                (?:\n           [ ]*  \.\.\. .*)*)  # PS2 lines
            \n?
            # Want consists of any non-blank lines that do not start with PS1.
            (?P<want> (?:(?![ ]*$)    # Not a blank line
                        (?![ ]*```)  # Not end of a code block
                        (?![ ]*>>>)  # Not a line starting with PS1
                        .+$\n?       # But any other line
                    )*)
            """,
        re.MULTILINE | re.VERBOSE,
    )

    p = doctest.DocTestParser
    if p._EXAMPLE_RE == _ORIGINAL_EXAMPLE_RE:  # noqa: SLF001
        p._EXAMPLE_RE = _MD_EXAMPLE_RE  # noqa: SLF001
    elif p._EXAMPLE_RE == _MD_EXAMPLE_RE:  # noqa: SLF001
        pass
    else:
        parsermismatch = f"Unexpected doctest parser encountered. Expected {_ORIGINAL_EXAMPLE_RE}, got {p._EXAMPLE_RE}"  # noqa: SLF001
        raise ValueError(parsermismatch)
