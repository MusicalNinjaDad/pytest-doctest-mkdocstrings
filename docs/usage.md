# Usage

After installation you can invoke pytest with the command line option `--doctest-mdcodeblocks`

You also need to specifically add `--doctest-modules` and/or `--doctest-glob="*.md"` to actually run doctest in your pytest session.

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

then use `pytest --no-doctest-mdcodeblocks` to temporarily override the setting.