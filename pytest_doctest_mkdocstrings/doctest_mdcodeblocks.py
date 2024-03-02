"""Implements the following pytest hooks."""
import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """
    Adds a commandline flag to enable/disable handling of markdown codeblocks in doctests.
    
    Run by pytest during initialisation.
    """

    collectiongroup = parser.getgroup("doctest", description="Doctest parsing")
    collectiongroup.addoption(
        "--doctest-mdcodeblocks",
        action = "store_true",
        help = "Allow markdown codeblocks enclosed with triple-ticks (```) in doctests.",
    )
    collectiongroup.addoption(
        "--no-doctest-mdcodeblocks",
        action = "store_false",
        dest = "doctest_mdcodeblocks",
        help = "Disable allowing markdown codeblocks enclosed with triple-ticks (```) in doctests.",
    )


def pytest_sessionstart(session: pytest.Session) -> None:
    """
    Monkeypatches the regex in doctest.DocTestParser to consider the end of codeblock marker as the end of an example.

    Run by pytest before beginning test collection.
    """
    if not session.config.option.doctest_mdcodeblocks:
        return

    import doctest
    import re

    # https://github.com/python/cpython/blob/a0a8d9ffe0ddb0f55aeb02801f48e722c2660ed3/Lib/doctest.py#L613

    _ORIGINAL_EXAMPLE_RE = re.compile(
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

    _MD_EXAMPLE_RE = re.compile(
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
    if p._EXAMPLE_RE == _ORIGINAL_EXAMPLE_RE:
        p._EXAMPLE_RE = _MD_EXAMPLE_RE
    elif p._EXAMPLE_RE == _MD_EXAMPLE_RE:
        pass
    else:
        parsermismatch = f"Unexpected doctest parser encountered. Expected {_ORIGINAL_EXAMPLE_RE}, got {p._EXAMPLE_RE}"
        raise ValueError(parsermismatch)
