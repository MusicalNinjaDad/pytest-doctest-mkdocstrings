"""
Run 3 tests for different ini and commandline combinations.

All test files are under test/assets and copied using pytest in autouse fixtures defined in conftest.py

1. test_patch.py - check that the regex is patched in doctest.DocTestParser
2. codeblocks.py - check how --doctest-modules copes with both a codeblock and a non-codeblock example
3. docs.md - check how --doctest-golb=*.md copes with a markdown file including a pycon codeblock
"""

import pytest

# Need to wait for https://github.com/pytest-dev/pytest/pull/11298 before fully parameterising these tests

@pytest.mark.usefixtures("_ini_enabled")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"passed": 4},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 4},id="Duplication"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed" : 3, "passed": 1}, id="Override"),
    ],
)
def test_inioption_enabled(pytester, runoptions, results):
    """Test outcome when `--doctest-mdcodeblocks` is included in pytest.ini under addopts."""
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.usefixtures("_ini_disabled")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed": 3, "passed" : 1},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 4},id="Override"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed": 3, "passed" : 1}, id="Duplication"),
    ],
)
def test_inioption_disabled(pytester, runoptions, results):
    """Test outcome when `--no-doctest-mdcodeblocks` is included in pytest.ini under addopts."""
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results


@pytest.mark.usefixtures("_ini_nosetting")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed" : 3, "passed": 1},id="Default"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 4},id="Enabled"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed" : 3, "passed": 1}, id="Disabled"),
    ],
)
def test_inioption_notgiven(pytester, runoptions, results):
    """Test outcome when no relevant option is included in pytest.ini under addopts."""
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results
