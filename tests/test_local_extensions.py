import pytest


class TestChar:
    @pytest.mark.parametrize(
        "value,expected",
        [
            ("あ", True),
            ("Ａ", True),
            ("１", True),
            ("A", False),
            ("1", False),
            ("ı", False),
        ],
    )
    def test_detect_full_width_characters(self, value, expected):
        from local_extensions.rest import Char

        c = Char(value)

        actual = c.is_full_wide_char

        assert actual is expected

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("あ", 2),
            ("Ａ", 2),
            ("１", 2),
            ("A", 1),
            ("1", 1),
            ("ı", 1),
        ],
    )
    def test_get_the_displayed_length(self, value, expected):
        from local_extensions.rest import Char

        c = Char(value)

        actual = c.length

        assert actual == expected


class TestString:
    @pytest.mark.parametrize(
        "values,expected", [("あいうえお", 10), ("ABCDE", 5), ("あABC", 5)]
    )
    def test_get_the_displayed_length(self, values, expected):
        from local_extensions.rest import String

        s = String(values)

        actual = s.length

        assert actual == expected


class TestRestTitle0:
    @pytest.mark.parametrize(
        "title,expected",
        [
            (
                "あいうえお",
                """##########
あいうえお
##########""",
            ),
            (
                "ABCDE",
                """#####
ABCDE
#####""",
            ),
            (
                "あABC",
                """#####
あABC
#####""",
            ),
        ],
    )
    def test_return__rest_title0(self, title, expected):
        from local_extensions.rest import _rest_title0

        actual = _rest_title0(title)

        assert actual == expected
