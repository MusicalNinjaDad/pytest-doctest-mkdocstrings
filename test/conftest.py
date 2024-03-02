import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def _codeblocksini(pytester):
    inicontents = """
    [pytest]
    doctest-mdcodeblocks = true
    """

    pytester.makeini(inicontents)
