import doctest
import re

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

def test_patched():
    p = doctest.DocTestParser
    assert p._EXAMPLE_RE == _MD_EXAMPLE_RE