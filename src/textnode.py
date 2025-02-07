# inline text
#   Normal text
#   Bold text
#   Italic text
#   Code text
#   Links
#   Images

from enum import Enum
from typing import Self


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, type: TextType, url=None):
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other: Self):
        return (
            self.text == other.text
            and self.type == other.type
            and self.url == other.url
        )

    def __ne__(self, other: Self):
        return not self.__eq__(other)

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
