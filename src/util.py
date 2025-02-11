from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(node: TextNode) -> LeafNode:

    match node.type:
        case TextType.TEXT:
            return LeafNode(None, node.text)
        case TextType.BOLD:
            return LeafNode("b", node.text)
        case TextType.ITALIC:
            return LeafNode("i", node.text)
        case TextType.CODE:
            return LeafNode("code", node.text)
        case TextType.LINK:
            return LeafNode("a", node.text, {"href": node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": node.url, "alt": node.text})
        # i don't see how can happen
        # parsing the text to create the node will validate against TextType
        case _:
            raise ValueError("bad TextNode type")


def main():
    print("you are not supposed to run this module")


if __name__ == "__main__":
    main()
