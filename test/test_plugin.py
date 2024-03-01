def test_pytester(pytester):
    pytester.makepyfile(
        """
        def test_pass():
            assert True
            
        def test_fail():
            assert False
        """
    )

    result = pytester.runpytest()

    result.assert_outcomes(failed=1, passed=1)