import pytest


def test_pytester(pytester):
    pytester.makepyfile(
        """
        def test_pass():
            assert True
            
        def test_fail():
            assert False
        """  # noqa: COM812
    )

    result = pytester.runpytest()

    result.assert_outcomes(failed=1, passed=1)

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
