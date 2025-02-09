from typing import Self
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: dict[str, str] = None,
    ):
        super().__init__(tag, value, None, props)
        if value == None:
            raise ValueError("leaf nodes must have a value")

    def to_html(self):
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
