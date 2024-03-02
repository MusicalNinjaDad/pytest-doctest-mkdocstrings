import pytest

# Need to wait for https://github.com/pytest-dev/pytest/pull/11298 before fully parameterising these tests

@pytest.mark.usefixtures("_codeblocksini")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"passed": 1},id="No override"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 1},id="Duplication"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed":1}, id="Override"),
    ],
)
def test_inioption_set(pytester, runoptions, results):
    pytester.copy_example("test_patch.py")
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results

@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"failed": 1},id="Default"),
        pytest.param("--doctest-mdcodeblocks", {"passed": 1},id="Enabled"),
        pytest.param("--no-doctest-mdcodeblocks", {"failed":1}, id="Disabled"),
    ],
)
def test_noini(pytester, runoptions, results):
    pytester.copy_example("test_patch.py")
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results
