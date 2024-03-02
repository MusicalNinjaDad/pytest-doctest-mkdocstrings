import pytest

# Need to wait for https://github.com/pytest-dev/pytest/pull/11298 before fully parameterising these tests

def test_patch(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest("--doctest-mdcodeblocks")
    result.assert_outcomes(passed=1)

def test_nopatch(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest()
    result.assert_outcomes(failed=1)

@pytest.mark.usefixtures("_codeblocksini")
@pytest.mark.parametrize(("runoptions", "results"),
    [
        pytest.param("", {"passed": 1},id="No override"),
    ],
)
def test_inioption_set(pytester, runoptions, results):
    pytester.copy_example("test_patch.py")
    testresult = pytester.runpytest(runoptions)
    assert testresult.parseoutcomes() == results


@pytest.mark.usefixtures("_codeblocksini")
def test_override_inioption(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest("--no-doctest-mdcodeblocks")
    result.assert_outcomes(failed=1)
