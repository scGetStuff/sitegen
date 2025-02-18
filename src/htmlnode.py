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

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props == None:
            return ""

        return "".join(
            # list(map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()))
            list(map(lambda item: f' {item}="{self.props[item]}"', self.props))
        )

    def __repr__(self) -> str:
        # return f"HTMLNode: <{self.tag}{self.props_to_html()}>\nchildren:{len(self.children) if self.children else 0}\nvalue:{self.value if self.value else ""}"
        return (
            f"HTMLNode: <{self.tag}{self.props_to_html()}>"
            f"\nchildren:{len(self.children) if self.children else 0}"
            f"\nvalue:{self.value if self.value else ""}"
        )
