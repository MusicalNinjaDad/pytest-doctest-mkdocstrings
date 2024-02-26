# noqa: D100

def pytest_sessionstart(session) -> None:  # noqa: ANN001, ARG001
    """
    Monkeypatches DocTests Regex to ignore end of codeblock marker.

    Run by pytest before beginning collection
    """
    import doctest
    import re

# https://github.com/python/cpython/blob/a0a8d9ffe0ddb0f55aeb02801f48e722c2660ed3/Lib/doctest.py#L613

    _ORIGINAL_EXAMPLE_RE = re.compile(r"""
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
        """, re.MULTILINE | re.VERBOSE)  # noqa: N806

    _MD_EXAMPLE_RE = re.compile(r"""
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
            """, re.MULTILINE | re.VERBOSE)  # noqa: N806

    p = doctest.DocTestParser
    assert p._EXAMPLE_RE == _ORIGINAL_EXAMPLE_RE  # noqa: S101, SLF001
    p._EXAMPLE_RE = _MD_EXAMPLE_RE  # noqa: SLF001
