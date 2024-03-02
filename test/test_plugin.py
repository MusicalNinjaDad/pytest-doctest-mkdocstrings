import pytest

# Need to wait for https://github.com/pytest-dev/pytest/pull/11298 before fully parameterising these tests

@pytest.mark.usefixtures("_codeblocksini", "_testfile")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"passed": 1},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 1},id="Duplication"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed":1}, id="Override"),
    ],
)
def test_inioption_set(pytester, runoptions, results):
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.usefixtures("_testfile")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed": 1},id="Default"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 1},id="Enabled"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed":1}, id="Disabled"),
    ],
)
def test_noini(pytester, runoptions, results):
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.usefixtures("_disabledcodeblocksini", "_testfile")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed": 1},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 1},id="Override"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed":1}, id="Duplication"),
    ],
)
def test_inioption_disabled(pytester, runoptions, results):
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.usefixtures("_pyfile", "_nosettingini")
def test_docstrings(pytester):
    testresult = pytester.runpytest()
    assert testresult.parseoutcomes() == {"passed": 1, "failed": 1}
