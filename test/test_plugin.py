import pytest


def test_patch(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest("--doctest-mdcodeblocks")
    result.assert_outcomes(passed=1)

def test_nopatch(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest()
    result.assert_outcomes(failed=1)

@pytest.mark.usefixtures("_codeblocksini")
def test_inioption(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


@pytest.mark.usefixtures("_codeblocksini")
def test_override_inioption(pytester):
    pytester.copy_example("test_patch.py")
    result = pytester.runpytest("--no-doctest-mdcodeblocks")
    result.assert_outcomes(failed=1)
