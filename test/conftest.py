import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def _codeblocksini(pytester):
    inicontents = """
    [pytest]
    addopts = --doctest-mdcodeblocks
    """

    pytester.makeini(inicontents)

@pytest.fixture
def _disabledcodeblocksini(pytester):
    inicontents = """
    [pytest]
    addopts = --no-doctest-mdcodeblocks
    """

    pytester.makeini(inicontents)

@pytest.fixture
def _testfile(pytester):
    pytester.copy_example("test_patch.py")