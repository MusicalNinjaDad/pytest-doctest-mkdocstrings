import pytest

# Need to wait for https://github.com/pytest-dev/pytest/pull/11298 before fully parameterising these tests

@pytest.mark.usefixtures("_codeblocksini")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"passed": 3},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 3},id="Duplication"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed" : 2, "passed": 1}, id="Override"),
    ],
)
def test_inioption_set(pytester, runoptions, results):
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.usefixtures("_nosettingini")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed" : 2, "passed": 1},id="Default"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 3},id="Enabled"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed" : 2, "passed": 1}, id="Disabled"),
    ],
)
def test_noini(pytester, runoptions, results):
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.usefixtures("_disabledcodeblocksini")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed": 2, "passed" : 1},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 3},id="Override"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed": 2, "passed" : 1}, id="Duplication"),
    ],
)
def test_inioption_disabled(pytester, runoptions, results):
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results
