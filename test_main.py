from password_checker.main import check_password_strength


def test_too_short_password():
    assert "too short" in check_password_strength("123")


def test_only_numbers():
    assert "must mix" in check_password_strength("12345678")


def test_only_letters():
    assert "must mix" in check_password_strength("abcdefgh")


def test_only_lowercase():
    assert "add both upper and lower" in check_password_strength("abcd1234")


def test_only_uppercase():
    assert "add both upper and lower" in check_password_strength("ABCD1234")


def test_strong_password():
    assert "Strong" in check_password_strength("GoodPass123!")
