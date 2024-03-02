import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def _ini_enabled(pytester):
    inicontents = """
    [pytest]
    addopts = --doctest-mdcodeblocks --doctest-modules --doctest-glob="*.md"
    """
    pytester.makeini(inicontents)

@pytest.fixture
def _ini_disabled(pytester):
    inicontents = """
    [pytest]
    addopts = --no-doctest-mdcodeblocks --doctest-modules --doctest-glob="*.md"
    """
    pytester.makeini(inicontents)

@pytest.fixture
def _ini_nosetting(pytester):
    inicontents = """
    [pytest]
    addopts = --doctest-modules --doctest-glob="*.md"
    """
    pytester.makeini(inicontents)

@pytest.fixture(autouse=True)
def _testfile(pytester):
    pytester.copy_example("test_patch.py")

@pytest.fixture(autouse=True)
def _pyfile(pytester):
    pytester.copy_example("codeblocks.py")

@pytest.fixture(autouse=True)
def _mdfile(pytester):
    pytester.copy_example("docs.md")
