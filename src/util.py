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
        case _:
            raise ValueError("bad TextNode type")


# inline code, bold, and italic text; pairs of delimiter
def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType,
) -> list[TextNode]:

    out: list[TextNode] = []

    for node in old_nodes:

        if node.type != TextType.TEXT:
            out.append(node)
            continue

        # TODO: not sure if this is an issue
        if not node.text:
            continue
            # raise Exception("empty input")

        # validate open and close delimiter
        indexes = []
        index = node.text.find(delimiter)
        while index != -1:
            indexes.append(index)
            index = node.text.find(delimiter, index + 1)
        if len(indexes) < 2 or len(indexes) % 2 != 0:
            raise Exception("missing delimiter")

        # use indexes to slice pieces of the string into nodes
        start = 0
        stop = len(node.text) - 1
        for i in range(0, len(indexes), 2):

            # left text before delimiter
            if indexes[i] > start:
                left = node.text[start : indexes[i]]
                out.append(TextNode(left, TextType.TEXT))
                # print(f"LEFT: '{left}'")

            # this is the special part: bold ...
            start = indexes[i] + len(delimiter)
            stop = indexes[i + 1]
            mid = node.text[start:stop]
            # print(f"MID: '{mid}'")
            out.append(TextNode(mid, text_type))
            # reset for next loop
            start = stop + len(delimiter)

        # add any trailing text
        start = stop + len(delimiter)
        stop = len(node.text)
        tail = node.text[start:stop]
        # print(f"TAIL: '{tail}'")
        if tail:
            out.append(TextNode(tail, TextType.TEXT))

    return out


def main():
    print("you are not supposed to run this module")


if __name__ == "__main__":
    main()
