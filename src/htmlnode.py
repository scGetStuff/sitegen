# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won’t have any attributes

from typing import Self


class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[Self] = None,
        props: dict[str, str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join(
            list(map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()))
        )

    def __repr__(self):
        s = f"HTMLNode: <{self.tag}{self.props_to_html()}>\nchildren:{ \
            len(self.children) if self.children else 0}\nvalue:{self.value}"
        return s
