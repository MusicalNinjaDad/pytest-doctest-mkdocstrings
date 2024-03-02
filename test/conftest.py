import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def _codeblocksini(pytester):
    inicontents = """
    [pytest]
    addopts = --doctest-mdcodeblocks
    """

    pytester.makeini(inicontents)
