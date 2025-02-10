from enum import Enum
from typing import Self


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, type: TextType, url: str = None):
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other: Self) -> bool:
        return (
            self.text == other.text
            and self.type == other.type
            and self.url == other.url
        )

    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
