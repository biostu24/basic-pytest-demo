import pytest
from is_prime import is_prime, __prime_checker__


class TestIsPrime(object):
    def test_fail_on_decimal(self):
        with pytest.raises(ValueError):
            is_prime(3.1)

    def test_pass_on_integer_float(self):
        is_prime(3.0)


    def test_negative_is_undefined(self):
        with pytest.raises(ValueError):
            is_prime(-1)

    def test_zero_is_undefined(self):
        with pytest.raises(ValueError):
            is_prime(0)

    def test_1_is_not_prime(self):
        assert is_prime(1) is False

    def test_2_is_prime(self):
        assert is_prime(2) is True

    def test_primes(self):
        # test first 10 prime numbers (non-edge case)
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
        assert is_prime(17) is True
        assert is_prime(19) is True
        assert is_prime(23) is True
        assert is_prime(29) is True

        # Two large prime numbers near 1e6
        assert is_prime(999979) is True
        assert is_prime(999983) is True

    def test_large_primes(self):
        assert is_prime(10000169) is True  # 1e8
        assert is_prime(100000007) is True  # 1e9
        assert is_prime(1000000007) is True  # 1e10
        assert is_prime(10000000019) is True  # 1e11
        assert is_prime(100123456789) is True  # 1e12
        assert is_prime(1000000000039) is True  # 1e13
        assert is_prime(10000000000283) is True  # 1e14
        assert is_prime(100110101011001) is True  # 1e15

    def test_non_primes(self):
        # test first 10 non-prime numbers (non-edge case)
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
        assert is_prime(12) is False
        assert is_prime(14) is False
        assert is_prime(15) is False
        assert is_prime(16) is False
        assert is_prime(18) is False

        # And two large odd non-prime numbers near 1e6
        assert is_prime(999977) is False
        assert is_prime(999981) is False


class TestPrimeChecker(object):
    def test_check_prime(self):
        assert __prime_checker__(7, 5) is True
        assert __prime_checker__(11, 9) is True

    def test_check_none_prime(self):
        assert __prime_checker__(10, 7) is False
        assert __prime_checker__(14, 9) is False
        assert __prime_checker__(21, 9) is False
