from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] = None,
    ):
        super().__init__(tag, "", children, props)

    def to_html(self) -> str:
        if self.tag == None:
            raise ValueError("parent nodes must have a tag")

        if self.children == None:
            raise ValueError("parent nodes must have children")

        return (
            f"<{self.tag}{self.props_to_html()}>{self.value}{self.kids()}</{self.tag}>"
        )

    def kids(self) -> str:
        return "".join(list(map(lambda kid: kid.to_html(), self.children)))
