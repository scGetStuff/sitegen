from textnode import TextNode, TextType
from leafnode import LeafNode
import re


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


# inline `code`, `bold`, and `italic` text; pairs of delimiter
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
        if not node.text:
            continue

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

            # add the node: `bold` ...
            start = indexes[i] + len(delimiter)
            stop = indexes[i + 1]
            mid = node.text[start:stop]
            out.append(TextNode(mid, text_type))

            # reset for next loop
            start = stop + len(delimiter)

        # add any trailing text
        stop = len(node.text)
        tail = node.text[start:stop]
        if tail:
            out.append(TextNode(tail, TextType.TEXT))

    return out


# This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    # TODO: this pattern makes `[` or `]` break stuff
    altPattern = r"!\[([^\[\]]*)\]"
    srcPattern = r"\(([^\(\)]*)\)"

    return re.findall(altPattern + srcPattern, text)


# This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    textPattern = r"\[([^\[\]]*)\]"
    hrefPattern = r"\(([^\(\)]*)\)"
    excludePattern = r"(?<!!)"

    return re.findall(excludePattern + textPattern + hrefPattern, text)


# ![rick roll](https://i.imgur.com/aKaOqIh.gif)
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    out: list[TextNode] = []

    for node in old_nodes:
        text = node.text

        imgs = extract_markdown_images(node.text)
        for img in imgs:
            parts = text.split(f"![{img[0]}]({img[1]})", 1)

            # if there is leading text
            if parts[0]:
                out.append(TextNode(parts[0], TextType.TEXT))

            # add the image
            out.append(TextNode(img[0], TextType.IMAGE, img[1]))

            # reset start for next image
            text = parts[1]

        # add any trailing text
        if text:
            out.append(TextNode(text, TextType.TEXT))

    return out


# [to boot dev](https://www.boot.dev)
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    out: list[TextNode] = []

    for node in old_nodes:
        text = node.text

        links = extract_markdown_links(node.text)
        for link in links:
            parts = text.split(f"[{link[0]}]({link[1]})", 1)

            # if there is leading text
            if parts[0]:
                out.append(TextNode(parts[0], TextType.TEXT))

            # add the link
            out.append(TextNode(link[0], TextType.LINK, link[1]))

            # reset start for next link
            text = parts[1]

        # add any trailing text
        if text:
            out.append(TextNode(text, TextType.TEXT))

    return out


def main():
    print("you are not supposed to run this module")


if __name__ == "__main__":
    main()
