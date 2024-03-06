# Usage

After installation you can invoke pytest with the command line option `--doctest-mdcodeblocks`

You also need to specifically add `--doctest-modules` and/or `--doctest-glob="*.md"` to actually run doctest in your pytest session.


## Installation

1. **Strongly recommended** to set up a virtual environment first! (e.g.. `python3 -m venv .venv`, `. .venv/bin/activate`)
1. Install with `pip install pytest-doctest-mkdocstrings`


## Command line

To run pytest and doctest all modules and all .md files:

```
`pytest --doctest-mdcodeblocks --doctest-modules --doctest-glob="*.md"`
```

## Project configuration

If you chose to add these options to your `pyproject.toml`, `pytest.ini`or similar:

```
[tool.pytest.ini_options]
addopts = [
    "--doctest-modules",
    "--doctest-glob='*.md'",
    "--doctest-mdcodeblocks"
]
```

## Disabling the plugin

You can completely disable the plugin by adding the command line option `-p no:doctest_mdcodeblocks` to pytest (via addopts or on the command line).

To override activation via pytest.ini for a specific test session use `pytest --no-doctest-mdcodeblocks` on the commandline.