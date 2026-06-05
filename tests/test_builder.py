"""Unit tests for the Yeomil Mono builder module."""

from yeomil_mono.builder import is_cjk


def test_is_cjk_korean_syllables() -> None:
    # U+AC00 (가) is a Hangul Syllable
    assert is_cjk(0xAC00) is True
    # U+D7A3 is the last Hangul Syllable
    assert is_cjk(0xD7A3) is True


def test_is_cjk_korean_jamo() -> None:
    # Hangul Jamo
    assert is_cjk(0x1100) is True
    # Hangul Compatibility Jamo
    assert is_cjk(0x3131) is True


def test_is_cjk_non_cjk() -> None:
    # Latin ASCII
    assert is_cjk(0x0061) is False  # 'a'
    assert is_cjk(0x0020) is False  # Space
    # Special symbols
    assert is_cjk(0x0021) is False  # '!'
