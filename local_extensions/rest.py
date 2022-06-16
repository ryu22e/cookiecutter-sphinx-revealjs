import unicodedata
from dataclasses import dataclass

from cookiecutter.utils import simple_filter


@dataclass(frozen=True)
class Char:
    value: str

    @property
    def is_full_wide_char(self) -> bool:
        return unicodedata.east_asian_width(self.value) in ["F", "W"]

    @property
    def length(self) -> int:
        return 2 if self.is_full_wide_char else 1


class String:
    def __init__(self, value: str):
        self._chars = [Char(s) for s in value]

    @property
    def length(self):
        return sum((c.length for c in self._chars))


def _rest_title0(title: str) -> str:
    s = String(title)
    length = s.length
    sharps = "#" * length
    return f"""{sharps}
{title}
{sharps}"""


@simple_filter
def rest_title0(title: str) -> str:
    return _rest_title0(title)
